from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import RegistroView, PerfilView, login_view, registro_view

urlpatterns = [
    # Vistas HTML (las páginas visuales)
    path('', login_view, name='login'),
    path('registro/', registro_view, name='registro'),

    # Endpoints de la API REST y JWT
    path('api/registro/', RegistroView.as_view(), name='api_registro'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/perfil/', PerfilView.as_view(), name='api_perfil'),
]