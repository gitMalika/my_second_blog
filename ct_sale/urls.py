from . import views
from django.urls import path

name_app = 'ct_sale'
urlpatterns = [
    path('', views.ct_render, name='ct_render'),
]