from django.urls import path, include
from . import views


urlpatterns = [
path('', views.home, name='home'),
path('save/', views.save_data, name='save'),
path('delete/', views.delete_data, name='delete'),
path('edit/', views.edit_data, name='edit'),





]