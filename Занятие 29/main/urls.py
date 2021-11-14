from django.urls import path
from social_network import settings

from . import views

urlpatterns = [
    path('logout', views.logout),
    path('reg', views.reg),
    path('login', views.login),
    path('subscribes/<str:username>/<str:action>', views.subscribes),
    path('news', views.news),
    path('media/<str:filename>', views.image),
    path('<str:username>', views.user),
    path('', views.index),

]
