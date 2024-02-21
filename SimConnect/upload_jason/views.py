from django.shortcuts import render
from .models import JsonData, FlightData
import datetime
import json

def index(request):
    if request.GET.get("page", "") == "table":
        return render(request, "table.html", {
            "data": JsonData.objects.values_list
        })
    if request.GET.get("page", "") == "testpage":
        FlightData.objects.create(
            x = 1.2,
            y = 5.4,
            z = 6.9,
            packetTime = datetime.datetime.now()
        )

        result = FlightData.objects.values()             # return ValuesQuerySet object
        list_result = [entry for entry in result]  # converts ValuesQuerySet into Python list
        print(list_result[0])
        return render(request, "test.html", {
            "data": list_result
        })
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        data = json_file.read().decode('utf-8')
        JsonData.objects.create(data=data).save()
        return render(request, 'success.html', {
            "testVersion": data
        })
    return render(request, "upload.html")


