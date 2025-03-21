from django.urls import path
from .views import register_user, signup, home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registeruser/', register_user, name='registeruser'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',signup,name='signup'),
    path('',home,name='home'),
]
