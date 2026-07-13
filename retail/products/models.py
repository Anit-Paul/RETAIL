from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.CharField(
    max_length=50,
    unique=True,
    editable=False
    )
    name = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    brand = models.CharField(max_length=100, blank=True)

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    current_stock = models.PositiveIntegerField(default=0)

    minimum_stock = models.PositiveIntegerField(default=10)

    expiry_date = models.DateField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.product_id:
            last_product = Product.objects.order_by('-id').first()

            if last_product:
                last_id = int(last_product.product_id.replace("PROD", ""))
                self.product_id = f"PROD{last_id + 1:03d}"
            else:
                self.product_id = "PROD001"

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name