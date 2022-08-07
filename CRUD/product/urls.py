from django import views
from django.urls import path

from . import views

urlpatterns =[
    #mixins
    #path('', views.ProductMixin.as_view()),
    #path('<int:pk>/', views.ProductMixin.as_view()),

    #function based
    #path('<int:pk>/', views.profuct_view),
    #path('', views.profuct_view),

    #class based
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
]