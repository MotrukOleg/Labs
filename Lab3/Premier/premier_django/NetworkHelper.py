# NetworkHelper.py
import requests

class NetworkHelper:


    BASE_URL = 'http://127.0.0.1:8080/users'

    @staticmethod
    def get_list(endpoint):
        url = f"{NetworkHelper.BASE_URL}/{endpoint}/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка при запиті до API: {e}")
            return None

    @staticmethod
    def get_item(endpoint, item_id):
        url = f"{NetworkHelper.BASE_URLl}/{endpoint}/{item_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка при запиті до API: {e}")
            return None

    @staticmethod
    def delete_item(endpoint, item_id):
        url = f"{NetworkHelper.BASE_URL}/{endpoint}/{item_id}/"
        response = requests.delete(url)
        response.raise_for_status()
