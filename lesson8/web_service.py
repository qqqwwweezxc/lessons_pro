import requests

class WebService:
    """Class for fetching data from a web service"""

    def get_data(self, url: str) -> dict:
        """Fetch JSON data from the given URL"""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError as error:
            print(f"HTTP error: {error}")
            return {}
        except requests.RequestException as error:
            print(f"Request error: {error}")
            return {}
