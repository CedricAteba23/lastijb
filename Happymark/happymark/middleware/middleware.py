# Dans un nouveau fichier 'middleware/auth_middleware.py'
from django.conf import settings

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'Authorization' in request.headers:
            response['X-Auth-Token'] = request.headers['Authorization']
        return response