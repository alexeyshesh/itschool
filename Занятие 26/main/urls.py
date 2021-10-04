from django.urls import path

from . import views

urlpatterns = [
    path('reg/', views.reg),
    path('login/', views.login),
    path('users/<str:username>', views.user),
    path('', views.index),
]
