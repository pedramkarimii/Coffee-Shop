from django.contrib.auth.models import User
from django.db import models
from menu.models import Product, Table


# Create your models here.


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_items"
    )
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order_items"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("order", "product")

    @property
    def total_price_item(self):
        return self.quantity * self.product.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    paid_time = models.DateTimeField(null=True, blank=True, auto_now=True)
    objects = models.Manager()

    @property
    def total_price(self):
        total = 0
        for item in self.order_items.all():
            total += item.total_price_item
        return total

    @property
    def factor_code(self):
        return self.id + 1000

    def __str__(self):
        return f"ID: {self.id} | User: {self.user}"
