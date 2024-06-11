from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scheme/<int:scheme_id>/', views.scheme_details, name='scheme_details'),
    path('archived_schemes/', views.archived_schemes, name='archived_schemes'), 
]

