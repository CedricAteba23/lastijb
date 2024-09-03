from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('sponsor/',views.SponsorList.as_view()),
    path('sponsor/<int:pk>/', views.SponsorDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)