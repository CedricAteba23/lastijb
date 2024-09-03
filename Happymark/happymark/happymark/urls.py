"""
URL configuration for happymark project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
from django.contrib import admin
from django.urls import path, include, re_path
# from students import views
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('etudiant.urls')),
    path('api/', include('candidat.urls')),
    path('api1/', include('groupe.urls')),
    path('', include('jury.urls')),
    path('', include('jure.urls')),
    path('', include('sponsor.urls')),
    path('', include('media.urls')),
    path('', include('activite.urls')),
    path('', include('critere.urls')),
    path('', include('note.urls')),
    path('', include('autentication.urls')),
    path(('users/'), include('users.urls')),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)