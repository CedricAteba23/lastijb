from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('jury/',views.Jurylist.as_view()),
    path('jury/<int:pk>/', views.JuryDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)