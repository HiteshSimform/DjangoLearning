from django.urls import path
from .views import hello_world, my_view
urlpatterns = [
    path('hello/',hello_world,name='hello-world'),
    path('my-view/', my_view, name='my-view'),
]