from django.db import models


# Create your models here.
class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=100)
    assigned_to = models.CharField(30)
    priority = models.IntegerField()
