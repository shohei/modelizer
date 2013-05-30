from django.db import models

# Create your models here.

class Camfile(models.Model):
    milData = models.TextField()
    drlData = models.TextField()
    dimData = models.TextField()
    
    


