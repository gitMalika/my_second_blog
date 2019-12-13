from . import views
from django.urls import path

name_app = 'coverage'
urlpatterns = [
    path('', views.coverage_render, name='coverage_render'),
]