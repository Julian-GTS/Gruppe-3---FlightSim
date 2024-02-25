from django.shortcuts import render
from django.http import JsonResponse
from .models import JsonData, FlightData
import json
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        data = json_file.read().decode('utf-8')
        JsonData.objects.create(data=data, timestamp=timezone.now()).save()
        return render(request, 'success.html', {
            "data": data
        })
    return render(request, "upload.html")

def jsondata(request):
    list = JsonData.objects.values_list()
    result = {
        "data": [json.loads(entry[1]) for entry in list],
        "timestamps": [entry[2] for entry in list] 
    }
    return JsonResponse(result)

def flightdata(request):
    list_result = [entry for entry in FlightData.objects.values()] # converts ValuesQuerySet into Python list

    return JsonResponse({"data": list_result})