from django.db import models 

class JsonData(models.Model):
    data = models.JSONField()

class FlightData(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    packetTime = models.TimeField()


