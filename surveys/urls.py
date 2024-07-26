from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('gamble/', views.gamble_page, name='gamble'),
    path('diabetes/', views.diabetes_page, name='diabetes'),
]
