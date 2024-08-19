from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import HomeView, RegisterFormView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('auth/login', LoginView.as_view(template_name='apps/auth/login.html'), name='login'),
    path('auth/logout', LogoutView.as_view(template_name='apps/auth/login.html'), name='logout'),
    path('auth/register', RegisterFormView.as_view(), name='register'),

]


