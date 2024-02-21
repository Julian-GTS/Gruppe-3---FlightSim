from django.shortcuts import render
from django.http import JsonResponse
from .models import JsonData, FlightData
import json, datetime

def index(request):
    if request.GET.get("page", "") == "table":
        list = JsonData.objects.values_list()
        result = {
            "data": [json.loads(entry[1]) for entry in list],
            "timestamps": [entry[2] for entry in list] 
        }
        return JsonResponse(result)
    if request.GET.get("page", "") == "testpage":
        # FlightData.objects.create(
        #     x = 1.2,
        #     y = 5.4,
        #     z = 6.9,
        #     packetTime = datetime.datetime.now()
        # )

        list_result = [entry for entry in FlightData.objects.values()]  # converts ValuesQuerySet into Python list

        return JsonResponse({"data": list_result})
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        data = json_file.read().decode('utf-8')
        JsonData.objects.create(data=data, timestamp=datetime.datetime.now()).save()
        return render(request, 'success.html', {
            "testVersion": data
        })
    return render(request, "upload.html")


