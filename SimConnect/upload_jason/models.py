from django.db import models 

class JsonData(models.Model):
    data = models.JSONField()
    timestamp = models.DateTimeField()

class FlightData(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    packetTime = models.TimeField()


