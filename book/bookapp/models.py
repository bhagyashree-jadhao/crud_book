from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author_name=models.CharField(max_length=20)
    description=models.CharField(max_length=80)
    published_date=models.DateField()
    