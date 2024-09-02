from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.username  # Изменено для лучшего представления

    class Meta:
        ordering = ['name']


class Game(models.Model):
    title = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')



