from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

