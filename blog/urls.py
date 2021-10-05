from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index),
    url('loadmore/', views.loadmore),
]