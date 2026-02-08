from django.contrib import admin
from django.urls import path
from .views import AnimalListCreateView, AnimalDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('animals/', AnimalListCreateView.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    