from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('activite/',views.ActiviteList.as_view()),
    path('activite/<int:pk>/', views.ActiviteDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)