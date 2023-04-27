from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('home', views.home.as_view(), name='home'),
    path('aboutme', views.aboutme.as_view(), name='aboutme'),
    path('portfolio', views.portfolio.as_view(), name='portfolio'),
]
