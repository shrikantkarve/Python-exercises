import requests
import base64
import json
import urllib3

# Suppress InsecureRequestWarning if using self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ScaleClient:
    """
    Client for interacting with IBM Storage Scale REST API.
    Handles authentication and base HTTP methods.
    """
    def __init__(self, endpoint, username, password, verify_ssl=False):
        """
        Initialize the ScaleClient.

        Args:
            endpoint (str): The base URL of the Scale API (e.g., https://192.168.1.100:443)
            username (str): Username for authentication.
            password (str): Password for authentication.
            verify_ssl (bool): Whether to verify SSL certificates. Default is False.
        """
        self.base_url = endpoint.rstrip('/')
        self.username = username
        self.password = password
        self.verify_ssl = verify_ssl
        self.session = requests.Session()
        self._setup_auth()

    def _setup_auth(self):
        """Sets up Basic Authentication for the session."""
        self.session.auth = (self.username, self.password)
        self.session.verify = self.verify_ssl
        # Set default headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def get(self, path, params=None):
        """
        Perform a GET request.

        Args:
            path (str): The API path relative to base URL.
            params (dict): Query parameters.

        Returns:
            dict: The JSON response.
        
        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        url = f"{self.base_url}{path}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, path, data=None):
        """
        Perform a POST request.

        Args:
            path (str): The API path relative to base URL.
            data (dict): The JSON payload.

        Returns:
            dict: The JSON response.

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        url = f"{self.base_url}{path}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        # Some POST requests might return 204 No Content or similar
        if response.status_code == 204:
            return {}
        try:
            return response.json()
        except ValueError:
            return {}

    def delete(self, path):
        """
        Perform a DELETE request.

        Args:
            path (str): The API path relative to base URL.

        Returns:
            dict: The JSON response (if any).

        Raises:
            requests.exceptions.HTTPError: If the request fails.
        """
        url = f"{self.base_url}{path}"
        response = self.session.delete(url)
        response.raise_for_status()
        if response.status_code == 204:
            return {}
        try:
            return response.json()
        except ValueError:
            return {}
