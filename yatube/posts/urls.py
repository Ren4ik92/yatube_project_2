from django.urls import path
from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    path('posts/<slug>', views.group_posts),
]