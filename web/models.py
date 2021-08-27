from django.db import models
from django.db.models.deletion import CASCADE

class Reporter(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)    
    last_name =  models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Article(models.Model):
    headline = models.CharField(max_length=500)
    pubdate = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)