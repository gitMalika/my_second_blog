from . import views
from django.urls import path

name_app = 'bs_status'
urlpatterns = [
    path('', views.tech_render, name='tech_render'),
]