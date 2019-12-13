from . import views
from django.urls import path

name_app = 'stores'
urlpatterns = [
    path('', views.stores_render, name='stores_render'),
]