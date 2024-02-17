from django.db import models 

class SimConnectData(models.Model):
    data = models.JSONField()