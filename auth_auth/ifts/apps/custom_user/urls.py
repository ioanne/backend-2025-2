from django.urls import path
# Import relativo
# from .views import CustomLoginView, CustomLogoutView, RegisterView

# Import absoluto
from apps.custom_user.views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]