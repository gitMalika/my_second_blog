from . import views
from django.urls import path

name_app = 'regions'
urlpatterns = [
    path('', views.region_render, name='region_render'),
]
