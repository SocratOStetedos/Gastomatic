"""
test_users.py
-------------
Tests pour le endpoint /users de l'API JSONPlaceholder.

On valide ici la structure des données utilisateurs et
quelques règles métier simples (email valide, etc.)
"""

import pytest
from utils.api_client import get_resource


class TestGetUsers:
    """Tests sur la liste et le détail des utilisateurs."""

    def test_get_all_users_status_200(self):
        """La liste des utilisateurs doit répondre avec 200."""
        response = get_resource("/users")
        assert response.status_code == 200

    def test_get_all_users_is_list(self):
        """La réponse doit être une liste."""
        response = get_resource("/users")
        assert isinstance(response.json(), list)

    def test_get_all_users_count(self):
        """JSONPlaceholder contient exactement 10 utilisateurs."""
        response = get_resource("/users")
        data = response.json()
        assert len(data) == 10, f"Attendu 10 utilisateurs, reçu {len(data)}"

    def test_get_single_user_status_200(self):
        """Un utilisateur existant doit retourner 200."""
        response = get_resource("/users/1")
        assert response.status_code == 200

    def test_get_single_user_required_fields(self):
        """Vérifie que les champs obligatoires sont présents."""
        response = get_resource("/users/1")
        data = response.json()

        required_fields = ["id", "name", "username", "email", "address", "phone", "website", "company"]
        for field in required_fields:
            assert field in data, f"Champ manquant : '{field}'"

    def test_get_user_email_contains_at(self):
        """L'email d'un utilisateur doit contenir '@' (validation basique)."""
        response = get_resource("/users/1")
        data = response.json()

        assert "@" in data["email"], f"Email invalide : {data['email']}"

    def test_get_user_address_has_city(self):
        """L'adresse doit contenir un champ 'city'."""
        response = get_resource("/users/1")
        data = response.json()

        assert "city" in data["address"], "L'adresse devrait avoir un champ 'city'"

    def test_get_user_company_has_name(self):
        """La compagnie doit avoir un nom."""
        response = get_resource("/users/1")
        data = response.json()

        assert "name" in data["company"]
        assert len(data["company"]["name"]) > 0

    def test_get_nonexistent_user_returns_404(self):
        """Un utilisateur inexistant doit retourner 404."""
        response = get_resource("/users/9999")
        assert response.status_code == 404


class TestUserPostsRelation:
    """Tests de la relation entre utilisateurs et leurs posts."""

    def test_get_posts_by_user(self):
        """On doit pouvoir récupérer les posts d'un utilisateur via query param."""
        response = get_resource("/posts?userId=1")
        data = response.json()

        assert response.status_code == 200
        assert isinstance(data, list)
        assert len(data) > 0

    def test_posts_belong_to_correct_user(self):
        """Tous les posts retournés doivent appartenir à l'utilisateur demandé."""
        user_id = 1
        response = get_resource(f"/posts?userId={user_id}")
        data = response.json()

        # Vérifie que CHAQUE post a le bon userId
        for post in data:
            assert post["userId"] == user_id, \
                f"Post {post['id']} n'appartient pas à l'utilisateur {user_id}"
