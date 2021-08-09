from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('reports/', views.all_reports),
    path('reports/<int:report_id>', views.report),
    path('', views.index)
]
