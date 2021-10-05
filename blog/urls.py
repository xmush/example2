from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vylona/', views.vylona),
    path('budy/', views.budy),
    path('jordan/', views.jordan),
    path('flower/', views.flower),
]