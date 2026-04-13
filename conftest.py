"""
conftest.py
-----------
Fichier spécial de PyTest : il est lu automatiquement avant tous les tests.
On y définit des "fixtures" = des données ou objets partagés entre les tests.

Pense à une fixture comme à une fonction de préparation que PyTest injecte
automatiquement dans tes tests quand tu les nommes en paramètre.
"""

import pytest


@pytest.fixture
def sample_post_payload():
    """
    Fixture : fournit un exemple de payload pour créer un post.
    Réutilisable dans n'importe quel test qui en a besoin.
    """
    return {
        "title": "Mon titre de test",
        "body": "Contenu de mon article de test.",
        "userId": 1
    }


@pytest.fixture
def sample_user_payload():
    """
    Fixture : fournit un exemple de payload pour créer un utilisateur.
    """
    return {
        "name": "Alice Dupont",
        "username": "alice_d",
        "email": "alice@example.com"
    }


@pytest.fixture
def valid_post_id():
    """Fixture : un ID de post qui existe dans l'API."""
    return 1


@pytest.fixture
def invalid_post_id():
    """Fixture : un ID de post qui n'existe PAS dans l'API."""
    return 9999
