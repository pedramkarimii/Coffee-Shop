from django.db import models
from django.contrib.auth import get_user_model


class PaidOrderManager(models.Manager):
    def get_queryset(self):
        user_model = get_user_model()
        if user_model.is_authenticated:
            return super().get_queryset().filter(is_paid=True)
        else:
            return super().get_queryset().none()


class NotPaidOrderManager(models.Manager):
    def get_queryset(self):
        user_model = get_user_model()
        if user_model.is_authenticated:
            return super().get_queryset().filter(is_paid=False)
        else:
            return super().get_queryset().none()
