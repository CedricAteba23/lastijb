from django.urls import path
from .views import SponsorProxyView, SponsorDetailProxyView

urlpatterns = [
    path('sponsors/', SponsorProxyView.as_view(), name='sponsor-list'),
    path('sponsors/<int:pk>/', SponsorDetailProxyView.as_view(), name='sponsor-detail'),
]