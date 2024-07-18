from django.urls import path
from . import views

urlpatterns = [
    path('carlist/', views.CarlistList),
    path('carlist/<int:pk>/', views.cardetail),
]