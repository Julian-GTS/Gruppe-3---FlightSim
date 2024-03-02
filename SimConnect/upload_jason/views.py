from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import JsonData, FlightData
import json
from django.utils import timezone

def index(request):
    """
    Der Index des /upload_jason pfades sendet entweder
    das upload.html-template oder im falle einer POST-
    request das success.html-template. Im falle des
    uploads wird davon ausgegangen, dass der request
    body eine gültige JSON enthält. Diese wird in der
    Postgres-DB gespeichert und ist über die URL
    /view-raw?id=(ID) auszulesen. Die ID wird in der
    Render-Methode in das success.html-template eingesetzt.
    """
    # TODO validate json client-side and server-side
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        data = json_file.read().decode('utf-8')
        dbData = JsonData.objects.create(data=data, timestamp=timezone.localtime())
        dbData.save()
        dbId = str(dbData.id)
        return render(request, 'success.html', {
            "data": data,
            "rawUrl": "view-raw?id=" + dbId
        })
    return render(request, "upload.html")

def jsondata(request):
    """
    Zeigt den gesamten Inhalt des JsonData-Models
    """
    list = JsonData.objects.values_list()
    result = {
        "data": [json.loads(entry[1]) for entry in list],
        "timestamps": [entry[2] for entry in list] 
    }
    return JsonResponse(result)

def flightdata(request):
    """
    Zeigt den gesamten Inhalt des FlightData-Models
    """
    list_result = [entry for entry in FlightData.objects.values()]

    return JsonResponse({"data": list_result})

def viewRaw(request):
    """
    URL zum abrufen einzelner JsonData-Einträge per ID
    """
    # TODO Auth-based cookie to validate access to db entry
    response = JsonData.objects.get(id = request.GET.get("id", 0))

    response_data = {
        "data": json.loads(response.data),
        "timestamp": timezone.localtime().strftime("%d.%m.%Y %H:%M:%S"),
    }

    return JsonResponse(response_data)