# mon_projet/urls.py
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
    path('users/', include('admin.urls')),
    # path('', include("groupe.urls")),
    
    # path(('users/'), include('users.urls'))
    # Ajoutez d'autres URLs ici
    # path('password-reset/', PasswordResetView.as_view()),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)