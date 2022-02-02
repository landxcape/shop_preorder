from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=10)
    location = models.CharField(max_length=64)

    class Meta:
        ordering = ['name', 'location']

    def __str__(self) -> str:
        return self.name
