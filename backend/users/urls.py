from django.urls import path
from .views import RegisterView, protected_view, api_root
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', api_root, name='api-root'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('protected/', protected_view, name='protected'),  # <-- NUEVA RUTA AGREGADA
]
