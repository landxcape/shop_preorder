from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
