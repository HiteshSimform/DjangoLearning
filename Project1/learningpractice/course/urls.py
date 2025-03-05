from django.urls import path
from .views import courses

urlpatterns = [
    path('crs/', courses, name='courses'),
]
