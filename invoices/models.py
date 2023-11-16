from django.db import models


class Invoice(models.Model):
    number = models.CharField(max_length=30)
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)


