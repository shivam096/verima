import os
import requests


def get_token():
    """Get accounts' tokens from Secret Manager

    Args:
        email (str): Account's email

    Returns:
        dict: HTTP Headers
    """
    params = {
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": os.getenv("REFRESH_TOKEN"),
        "grant_type": "refresh_token",
    }
    with requests.post("https://oauth2.googleapis.com/token", params=params) as r:
        access_token = r.json()["access_token"]
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

