from django.db import models
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.models import User
from menu.models import Table


class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    repay_time = models.DateTimeField(null=True, blank=True, auto_now=True)