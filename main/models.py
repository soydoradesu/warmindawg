from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.name