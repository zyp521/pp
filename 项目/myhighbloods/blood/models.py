from django.db import models

# Create your models here.
class MyBlood(models.Model):
    username=models.CharField(max_length=20)
    sex=models.BooleanField(default=True)
    tall=models.DecimalField(max_digits=6,decimal_places=2)
    weight=models.DecimalField(max_digits=6,decimal_places=2)
    smoke=models.BooleanField(default=True)
    drink=models.BooleanField(default=True)
