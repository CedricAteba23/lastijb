from django.urls import path
from .views import RegisterOrganisateurView, CreateJuryView, CreateJuryPopulaireView, CustomTokenObtainPairView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterOrganisateurView.as_view(), name='register_organisateur'),
    path('create-jury/', CreateJuryView.as_view(), name='create_jury'),
    path('create-jury-populaire/', CreateJuryPopulaireView.as_view(), name='create_jury_populaire'),
]
