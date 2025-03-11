from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_form'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('view-all/', views.view_all_contacts, name='view_all_contacts'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
