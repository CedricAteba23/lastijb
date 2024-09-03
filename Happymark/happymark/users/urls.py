# from django.urls import path, re_path
# from .import views
# from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
# from dj_rest_auth.views import LoginView, LogoutView

# urlpatterns = [

#     path('list/', views.UserList.as_view()),
#     path('list/<int:pk>/', views.UserDetail.as_view()),

#     path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    
#     path('register/', RegisterView.as_view()),
#     path('login/', LoginView.as_view()),
#     path('logout/', LogoutView.as_view()),

#     path('verify-email/',
#          VerifyEmailView.as_view(), name='rest_verify_email'),
#     path('account-confirm-email/',
#          VerifyEmailView.as_view(), name='account_email_verification_sent'),
#     re_path('account-confirm-email/(?P<key>[-:\w]+)/$',
#          VerifyEmailView.as_view(), name='account_confirm_email'),
# ]
from django.urls import path
from .views import inscription, connexion, UtilisateurListAPIView, UtilisateurDetailAPIView, UtilisateurUpdateAPIView, UtilisateurDeleteAPIView

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('utilisateurs/', UtilisateurListAPIView.as_view(), name='utilisateur-list'),
    path('utilisateurs/<int:pk>/', UtilisateurDetailAPIView.as_view(), name='utilisateur-detail'),
    path('utilisateurs/<int:pk>/update/', UtilisateurUpdateAPIView.as_view(), name='utilisateur-update'),
    path('utilisateurs/<int:pk>/delete/', UtilisateurDeleteAPIView.as_view(), name='utilisateur-delete'),
]
