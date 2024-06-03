from django.urls import path
from . import views

urlpatterns = [
path('last/', views.hello_world, name='hello_world'),
path('test/', views.test, name='test'),
path('info/', views.info, name='info'),
path('', views.login, name='login'),
path('register/', views.register, name='register'),
]