from django.urls import path
from .views import myfunction

urlpatterns = [
    path('', myfunction, name='myfunction'),
]
