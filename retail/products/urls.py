from django.contrib import admin
from django.urls import path,include
from .views import categoryListView, CategoryDetailView

urlpatterns = [
    path('category/',categoryListView.as_view(),name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]