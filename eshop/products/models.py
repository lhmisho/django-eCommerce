from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    Price       = models.DecimalField(default=10.00, decimal_places=2, max_digits=19)

    def __str__(self):
        return self.title