from django.db import models


class DateAbstractModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True