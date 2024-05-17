from django.db import models
from .managers import ActiveProductManager, InactiveProductManager
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("Category", related_name="products")
    # active_objects = ActiveProductManager()
    # inactive_objects = InactiveProductManager()
    # objects = models.Manager()




    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu/category_images/", null=True, blank=True)
    sub_of = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"
