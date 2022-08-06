from django import views
from django.urls import path

from . import views

urlpatterns =[
    path('', views.ProductMixin.as_view()),
    path('<int:pk>/', views.ProductMixin.as_view()),
]