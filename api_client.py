"""
api_client.py
-------------
Client HTTP réutilisable pour tous nos tests.
Centralise les appels à l'API pour éviter la répétition de code.

API utilisée : JSONPlaceholder (https://jsonplaceholder.typicode.com)
C'est une fausse API REST gratuite, parfaite pour s'entraîner.
"""

import requests


# URL de base de l'API - on la définit une seule fois ici
BASE_URL = "https://jsonplaceholder.typicode.com"


def get_resource(endpoint: str) -> requests.Response:
    """
    Envoie une requête GET à l'API.

    Args:
        endpoint (str): Le chemin de la ressource, ex: "/posts/1"

    Returns:
        requests.Response: La réponse complète de l'API
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, timeout=10)
    return response


def create_resource(endpoint: str, payload: dict) -> requests.Response:
    """
    Envoie une requête POST à l'API pour créer une ressource.

    Args:
        endpoint (str): Le chemin de la ressource, ex: "/posts"
        payload (dict): Les données à envoyer au format JSON

    Returns:
        requests.Response: La réponse complète de l'API
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload, timeout=10)
    return response


def update_resource(endpoint: str, payload: dict) -> requests.Response:
    """
    Envoie une requête PUT à l'API pour modifier une ressource.

    Args:
        endpoint (str): Le chemin de la ressource, ex: "/posts/1"
        payload (dict): Les nouvelles données

    Returns:
        requests.Response: La réponse complète de l'API
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.put(url, json=payload, timeout=10)
    return response


def delete_resource(endpoint: str) -> requests.Response:
    """
    Envoie une requête DELETE à l'API.

    Args:
        endpoint (str): Le chemin de la ressource, ex: "/posts/1"

    Returns:
        requests.Response: La réponse complète de l'API
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.delete(url, timeout=10)
    return response
