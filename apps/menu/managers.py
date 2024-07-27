from django.db import models


class ActiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class InactiveProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)
