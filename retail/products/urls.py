from django.contrib import admin
from django.urls import path,include
from .views import categoryListView, CategoryDetailView,ProductListView,ProductDetailView,ProductCategoryView,AddStockView, StockHistoryView

urlpatterns = [
    path('category/',categoryListView.as_view(),name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path("products/category/<int:pk>/", ProductCategoryView.as_view(), name="product-category"),
    path(
    "products/<str:pk>/add-stock/",
    AddStockView.as_view(),
    name="add-stock"
    ),

    path(
        "products/<str:pk>/stock-history/",
        StockHistoryView.as_view(),
        name="stock-history"
    ),
]