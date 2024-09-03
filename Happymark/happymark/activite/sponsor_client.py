import requests




class SponsorClient:
    def __init__(self, base_url='http://localhost:8001/api'):
        # self.base_url = base_url
        pass

    def get_sponsors(self):
        response = requests.get(f'{self.base_url}/sponsors/')
        return response.json()

    def get_sponsor(self, sponsor_id):
        response = requests.get(f'{self.base_url}/sponsors/{sponsor_id}/')
        return response.json()