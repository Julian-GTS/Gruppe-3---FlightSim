from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import JsonData, FlightData
import json
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        data = json_file.read().decode('utf-8')
        dbData = JsonData.objects.create(data=data, timestamp=timezone.now())
        dbData.save()
        dbId = str(dbData.id)
        return render(request, 'success.html', {
            "data": data,
            "rawUrl": "view-raw?id=" + dbId
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
    list_result = [entry for entry in FlightData.objects.values()]

    return JsonResponse({"data": list_result})

def viewRaw(request):
    response = JsonData.objects.get(id = request.GET.get("id", 0))

    response_data = {
        "data": json.loads(response.data),
        "timestamp": response.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
    }

    return JsonResponse(response_data)