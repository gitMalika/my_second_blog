from . import views
from django.urls import path

name_app = 'map'
urlpatterns = [
    path('', views.index, name='index'),
]
