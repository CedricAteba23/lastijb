from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import requests

class SponsorProxyView(APIView):
    def get(self, request, format=None):
        # response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/")
        headers = {}
        if 'HTTP_AUTHORIZATION' in request.META:
            headers['Authorization'] = request.META['HTTP_AUTHORIZATION']
        response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/", headers=headers)
        return Response(response.json())
       
       

    def post(self, request, format=None):
        # response = requests.post(f"{settings.SPONSOR_SERVICE_URL}/sponsors/", json=request.data)
        headers = {}
        if 'HTTP_AUTHORIZATION' in request.META:
            headers['Authorization'] = request.META['HTTP_AUTHORIZATION']
        response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/", headers=headers)
        return Response(response.json())
        # return Response(response.json(), status=response.status_code)

class SponsorDetailProxyView(APIView):
    def get(self, request, pk, format=None):
        # response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/{pk}/")
        headers = {}
        if 'HTTP_AUTHORIZATION' in request.META:
            headers['Authorization'] = request.META['HTTP_AUTHORIZATION']
        response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/", headers=headers)
        # return Response(response.json())
        return Response(response.json())

    def put(self, request, pk, format=None):
        response = requests.put(f"{settings.SPONSOR_SERVICE_URL}/sponsors/{pk}/", json=request.data)
        return Response(response.json(), status=response.status_code)

    def delete(self, request, pk, format=None):
        response = requests.delete(f"{settings.SPONSOR_SERVICE_URL}/sponsors/{pk}/")
        return Response(status=response.status_code)
    

# def get(self, request, format=None):
#         headers = {}
#         if 'HTTP_AUTHORIZATION' in request.META:
#             headers['Authorization'] = request.META['HTTP_AUTHORIZATION']
#         response = requests.get(f"{settings.SPONSOR_SERVICE_URL}/sponsors/", headers=headers)
#         return Response(response.json())