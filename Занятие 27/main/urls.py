from django.urls import path

from . import views

urlpatterns = [
    path('logout', views.logout),
    path('reg', views.reg),
    path('login', views.login),
    path('subscribe/<str:username>', views.subscribe),
    path('<str:username>', views.user),
    path('', views.index),
]
