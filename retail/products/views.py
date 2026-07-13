from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, InventoryTransaction
from .serializers import CategorySerializer, ProductSerializer, InventoryTransactionSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class categoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Category, pk=pk)

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        category = self.get_object(pk)

        serializer = CategorySerializer(
            category,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
        
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        product = self.get_object(pk)

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
class ProductCategoryView(APIView):
    def get(self, request, pk):
        products = Product.objects.filter(category=pk)
        serializer = ProductSerializer(products, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

class AddStockView(APIView):

    def post(self, request, pk):
        product = get_object_or_404(Product, product_id=pk)

        quantity = request.data.get("quantity")
        remarks = request.data.get("remarks", "Stock added")

        if quantity is None:
            return Response(
                {"error": "Quantity is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return Response(
                {"error": "Quantity must be a valid integer"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if quantity <= 0:
            return Response(
                {"error": "Quantity must be greater than zero"},
                status=status.HTTP_400_BAD_REQUEST
            )

        product.current_stock += quantity
        print(product.current_stock)
        product.save(update_fields=["current_stock"])

        transaction = InventoryTransaction.objects.create(
            product=product,
            transaction_type="IN",
            quantity=quantity,
            remarks=remarks
        )

        return Response(
            {
                "message": "Stock added successfully",
                "product_id": product.id,
                "product_name": product.name,
                "added_quantity": quantity,
                "current_stock": product.current_stock,
                "transaction_id": transaction.id
            },
            status=status.HTTP_200_OK
        )
    
class StockHistoryView(APIView):

    def get(self, request, pk):
        product = get_object_or_404(Product, product_id=pk)

        transactions = InventoryTransaction.objects.filter(
            product=product
        ).order_by("-created_at")

        serializer = InventoryTransactionSerializer(
            transactions,
            many=True
        )

        return Response(
            {
                "product_id": product.id,
                "product_name": product.name,
                "current_stock": product.current_stock,
                "stock_history": serializer.data
            },
            status=status.HTTP_200_OK
        )