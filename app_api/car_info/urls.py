from django.urls import path
from .views import getCarInfo, getCarInfos, updateCarInfo, deleteCarInfo, addCarInfo

urlpatterns = [
    path('', getCarInfos),
    path('<str:pk>/', getCarInfo),
    path('api/add/', addCarInfo),
    path('api/<str:pk>/update', updateCarInfo),
    path('api/<str:pk>/delete', deleteCarInfo),
]
