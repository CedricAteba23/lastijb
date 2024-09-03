from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns=[
    path('groupes/',views.Groupelist.as_view()),
    path('groupes/<int:pk>/', views.GroupeDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)



# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from .import views

# urlpatterns = [
#     path('enquetes/', views.EnqueteList.as_view()),
#     path('enquetes/<int:pk>/', views.EnqueteDetail.as_view()),
    
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)