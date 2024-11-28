import requests

class APIClient:#абстрагує взаємодію з API
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def fetch_data(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching data from {url}: {e}")

    def fetch_users(self):
        return self.fetch_data("users")

    def fetch_posts(self):
        return self.fetch_data("posts")
