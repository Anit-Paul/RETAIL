from rest_framework import serializers
from .models import Category, Product, InventoryTransaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_id",
            "name",
            "category",
            "brand",
            "purchase_price",
            "selling_price",
            "current_stock",
            "minimum_stock",
            "expiry_date",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "product_id",
            "created_at",
            "updated_at",
        ]

class InventoryTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryTransaction
        fields = [
            "id",
            "transaction_type",
            "quantity",
            "remarks",
            "created_at"
        ]