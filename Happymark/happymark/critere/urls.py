from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('critere/',views.CritereList.as_view()),
    path('critere/<int:pk>/', views.CritereDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)