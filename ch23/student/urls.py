from django.urls import path
from .views import all_data
urlpatterns = [
    path('all/', all_data, name='all_data'),
]