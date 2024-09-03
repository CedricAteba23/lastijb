from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('media/',views.MediaList.as_view()),
    path('media/<int:pk>/', views.MediaDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)