from django.db import models 

class JsonData(models.Model):
    data = models.JSONField()

   
