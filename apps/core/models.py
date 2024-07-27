from django.db import models


class ActivateMixin(models.Model):
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True
