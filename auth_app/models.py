from django.db import models

# Create your models here.
class Book(models.Model):
    titel = models.CharField(max_length=100)
    author = models.CharField(max_length=100)    
    discription = models.TextField()
    published_year = models.PositiveBigIntegerField()
    groups = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)


class Group(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.titel