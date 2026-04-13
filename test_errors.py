"""
test_errors.py
--------------
Tests dédiés à la gestion des erreurs et des cas limites (edge cases).

Ces tests vérifient que l'API se comporte correctement
quand on lui envoie des données incorrectes ou inattendues.
C'est ce qu'on appelle les "tests négatifs" ou "sad path tests".
"""

import pytest
import requests
from utils.api_client import get_resource, create_resource


class TestNotFoundErrors:
    """Tests pour les ressources inexistantes (erreur 404)."""

    @pytest.mark.parametrize("endpoint", [
        "/posts/99999",
        "/users/99999",
        "/comments/99999",
    ])
    def test_inexistant_resources_return_404(self, endpoint):
        """
        Test paramétré : vérifie que plusieurs endpoints inexistants
        retournent tous un code 404.

        @pytest.mark.parametrize = le même test s'exécute plusieurs fois
        avec des valeurs différentes. Très pratique !
        """
        response = get_resource(endpoint)
        assert response.status_code == 404, \
            f"'{endpoint}' devrait retourner 404, reçu {response.status_code}"


class TestResponseFormat:
    """Tests sur le format des réponses."""

    def test_response_content_type_is_json(self):
        """La réponse doit avoir un Content-Type JSON."""
        response = get_resource("/posts/1")

        # On vérifie l'en-tête HTTP Content-Type
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type, \
            f"Content-Type attendu : application/json, reçu : {content_type}"

    def test_response_time_is_acceptable(self):
        """Le temps de réponse doit être inférieur à 3 secondes."""
        response = get_resource("/posts")

        # response.elapsed = durée réelle de la requête
        elapsed_seconds = response.elapsed.total_seconds()
        assert elapsed_seconds < 3.0, \
            f"Temps de réponse trop long : {elapsed_seconds:.2f}s (max 3s)"

    def test_json_is_parseable(self):
        """La réponse doit être du JSON valide et parsable."""
        response = get_resource("/posts/1")

        try:
            data = response.json()
            assert data is not None
        except requests.exceptions.JSONDecodeError as e:
            pytest.fail(f"La réponse n'est pas du JSON valide : {e}")


class TestDataValidation:
    """Tests de validation des données retournées."""

    def test_post_id_is_integer(self):
        """L'ID d'un post doit être un entier, pas une chaîne."""
        response = get_resource("/posts/1")
        data = response.json()

        assert isinstance(data["id"], int), \
            f"L'ID devrait être un entier, reçu : {type(data['id'])}"

    def test_post_user_id_is_positive(self):
        """Le userId d'un post doit être un entier positif."""
        response = get_resource("/posts/1")
        data = response.json()

        assert data["userId"] > 0, "userId devrait être positif"

    def test_all_posts_have_non_empty_title(self):
        """Tous les posts doivent avoir un titre non vide."""
        response = get_resource("/posts")
        posts = response.json()

        for post in posts:
            assert post.get("title"), \
                f"Le post {post.get('id')} a un titre vide ou manquant"

    def test_create_post_with_empty_payload(self):
        """
        Envoyer un payload vide ne doit pas planter notre code.
        Note : JSONPlaceholder retourne quand même 201 car c'est une fausse API,
        mais en prod, on s'attendrait à un 400 (Bad Request).
        """
        response = create_resource("/posts", {})

        # On vérifie juste que la requête n'a pas levé d'exception
        assert response.status_code in [200, 201, 400], \
            f"Code de statut inattendu pour payload vide : {response.status_code}"
