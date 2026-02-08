
from django.urls import path
from .views import VehicleListCreate, VehicleDetailView

urlpatterns = [
    path('vehicles/', VehicleListCreate.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
]
