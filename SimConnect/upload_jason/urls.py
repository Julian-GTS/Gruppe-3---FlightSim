from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jsondata", views.jsondata, name="json-data"),
    path("flightdata", views.flightdata, name="flight-data")
]