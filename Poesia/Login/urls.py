from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='Login/login.html'), name="Login"),
    path('logout/', LogoutView.as_view(template_name='Login/logout.html'), name='Logout')
]