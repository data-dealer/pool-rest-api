from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('pool', views.PoolEndPoint, name='pool'),
    path('poolQuantile', views.PoolQuantileEndPoint, name='poolQuantile'),
]

