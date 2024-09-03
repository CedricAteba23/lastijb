from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('candidats/',views.Candidatlist.as_view()),
    path('candidats/<int:pk>/', views.CandidatDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)