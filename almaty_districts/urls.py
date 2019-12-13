from . import views
from django.urls import path

name_app = 'almaty_districts'
urlpatterns = [
    path('', views.district_render, name='district_render'),
]
