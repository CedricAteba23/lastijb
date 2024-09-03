from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('note/',views.ActiviteGroupeList.as_view()),
    path('note/<int:pk>/', views.ActiviteGroupeDetail.as_view())
    # path('groupes/<int:pk>/', views.GroupeDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)