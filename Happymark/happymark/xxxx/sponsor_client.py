import requests

class SponsorClient:
    def __init__(self, base_url='http://localhost:8001/api'):
        self.base_url = base_url

    def get_sponsors(self):
        response = requests.get(f'{self.base_url}/sponsors/')
        return response.json()

    def get_sponsor(self, sponsor_id):
        response = requests.get(f'{self.base_url}/sponsors/{sponsor_id}/')
        return response.json()

    def create_sponsor(self, data):
        response = requests.post(f'{self.base_url}/sponsors/', json=data)
        return response.json()

    def update_sponsor(self, sponsor_id, data):
        response = requests.put(f'{self.base_url}/sponsors/{sponsor_id}/', json=data)
        return response.json()

    def delete_sponsor(self, sponsor_id):
        response = requests.delete(f'{self.base_url}/sponsors/{sponsor_id}/')
        return response.status_code == 204