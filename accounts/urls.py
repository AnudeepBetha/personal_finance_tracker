from django.urls import path
from .views import register,dashboard, update_profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('update-profile/', update_profile, name='update_profile'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]