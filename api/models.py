from django.db import models

# Create your models here.
class todo(models.Model):
    date=models.DateField(auto_created=True)
    task=models.CharField(max_length=50)