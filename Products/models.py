from django.db import models

# Create your models here.


class ItemType(models.Model):
    item_type = models.CharField(max_length=50)

    def __str__(self):
        return self.item_type


class Product(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    image = models.CharField(max_length=2048)
    price = models.FloatField()
    quantity = models.IntegerField()
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title