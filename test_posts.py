"""
test_posts.py
-------------
Tests pour le endpoint /posts de l'API JSONPlaceholder.

On teste ici les opérations CRUD :
  - GET  : lire un post ou une liste de posts
  - POST : créer un nouveau post
  - PUT  : modifier un post existant
  - DELETE : supprimer un post

Convention de nommage PyTest : les fonctions de test DOIVENT commencer par test_
"""

import pytest
from utils.api_client import get_resource, create_resource, update_resource, delete_resource


# ─────────────────────────────────────────────
# Tests GET
# ─────────────────────────────────────────────

class TestGetPosts:
    """Groupe de tests pour les requêtes GET sur /posts"""

    def test_get_all_posts_status_code(self):
        """Vérifie que la liste des posts répond avec un code 200 (OK)."""
        response = get_resource("/posts")

        # assert = "Je certifie que cette condition est vraie"
        assert response.status_code == 200, \
            f"Attendu 200, reçu {response.status_code}"

    def test_get_all_posts_returns_list(self):
        """Vérifie que la réponse est bien une liste."""
        response = get_resource("/posts")
        data = response.json()

        assert isinstance(data, list), "La réponse devrait être une liste"

    def test_get_all_posts_not_empty(self):
        """Vérifie que la liste contient au moins un élément."""
        response = get_resource("/posts")
        data = response.json()

        assert len(data) > 0, "La liste des posts ne devrait pas être vide"

    def test_get_single_post_status_code(self, valid_post_id):
        """Vérifie qu'un post existant répond avec un code 200."""
        response = get_resource(f"/posts/{valid_post_id}")

        assert response.status_code == 200

    def test_get_single_post_has_required_fields(self, valid_post_id):
        """Vérifie que le JSON d'un post contient les champs attendus."""
        response = get_resource(f"/posts/{valid_post_id}")
        data = response.json()

        # Ces champs DOIVENT exister dans la réponse
        required_fields = ["id", "title", "body", "userId"]
        for field in required_fields:
            assert field in data, f"Champ manquant : '{field}'"

    def test_get_single_post_correct_id(self, valid_post_id):
        """Vérifie que l'ID retourné correspond à celui demandé."""
        response = get_resource(f"/posts/{valid_post_id}")
        data = response.json()

        assert data["id"] == valid_post_id

    def test_get_single_post_title_is_string(self, valid_post_id):
        """Vérifie que le titre est bien une chaîne de caractères."""
        response = get_resource(f"/posts/{valid_post_id}")
        data = response.json()

        assert isinstance(data["title"], str)
        assert len(data["title"]) > 0, "Le titre ne devrait pas être vide"

    def test_get_nonexistent_post_returns_404(self, invalid_post_id):
        """Vérifie qu'un post inexistant retourne un code 404 (Not Found)."""
        response = get_resource(f"/posts/{invalid_post_id}")

        assert response.status_code == 404, \
            f"Un ID invalide devrait retourner 404, reçu {response.status_code}"


# ─────────────────────────────────────────────
# Tests POST
# ─────────────────────────────────────────────

class TestCreatePost:
    """Groupe de tests pour les requêtes POST sur /posts"""

    def test_create_post_status_code(self, sample_post_payload):
        """Vérifie que la création d'un post retourne 201 (Created)."""
        response = create_resource("/posts", sample_post_payload)

        assert response.status_code == 201, \
            f"La création devrait retourner 201, reçu {response.status_code}"

    def test_create_post_returns_json(self, sample_post_payload):
        """Vérifie que la réponse est du JSON valide."""
        response = create_resource("/posts", sample_post_payload)

        # Si le JSON est invalide, .json() lèvera une exception → test échoue
        data = response.json()
        assert data is not None

    def test_create_post_has_id(self, sample_post_payload):
        """Vérifie que le post créé reçoit un ID de l'API."""
        response = create_resource("/posts", sample_post_payload)
        data = response.json()

        assert "id" in data, "Le post créé devrait avoir un 'id'"

    def test_create_post_title_matches(self, sample_post_payload):
        """Vérifie que le titre envoyé est bien renvoyé dans la réponse."""
        response = create_resource("/posts", sample_post_payload)
        data = response.json()

        assert data["title"] == sample_post_payload["title"]

    def test_create_post_body_matches(self, sample_post_payload):
        """Vérifie que le body envoyé est bien renvoyé dans la réponse."""
        response = create_resource("/posts", sample_post_payload)
        data = response.json()

        assert data["body"] == sample_post_payload["body"]

    def test_create_post_user_id_matches(self, sample_post_payload):
        """Vérifie que l'userId envoyé est bien renvoyé dans la réponse."""
        response = create_resource("/posts", sample_post_payload)
        data = response.json()

        assert data["userId"] == sample_post_payload["userId"]


# ─────────────────────────────────────────────
# Tests PUT
# ─────────────────────────────────────────────

class TestUpdatePost:
    """Groupe de tests pour les requêtes PUT sur /posts/{id}"""

    def test_update_post_status_code(self, valid_post_id):
        """Vérifie que la mise à jour retourne un code 200."""
        payload = {
            "id": valid_post_id,
            "title": "Titre modifié",
            "body": "Contenu modifié.",
            "userId": 1
        }
        response = update_resource(f"/posts/{valid_post_id}", payload)

        assert response.status_code == 200

    def test_update_post_title_is_updated(self, valid_post_id):
        """Vérifie que le nouveau titre est bien présent dans la réponse."""
        new_title = "Nouveau titre après modification"
        payload = {
            "id": valid_post_id,
            "title": new_title,
            "body": "Contenu modifié.",
            "userId": 1
        }
        response = update_resource(f"/posts/{valid_post_id}", payload)
        data = response.json()

        assert data["title"] == new_title


# ─────────────────────────────────────────────
# Tests DELETE
# ─────────────────────────────────────────────

class TestDeletePost:
    """Groupe de tests pour les requêtes DELETE sur /posts/{id}"""

    def test_delete_post_status_code(self, valid_post_id):
        """Vérifie que la suppression retourne un code 200."""
        response = delete_resource(f"/posts/{valid_post_id}")

        assert response.status_code == 200

    def test_delete_post_returns_empty_body(self, valid_post_id):
        """Vérifie que la réponse de suppression est vide ({}). """
        response = delete_resource(f"/posts/{valid_post_id}")
        data = response.json()

        # JSONPlaceholder retourne {} pour confirmer la suppression
        assert data == {}
