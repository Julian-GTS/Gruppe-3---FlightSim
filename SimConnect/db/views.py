import json
from django.http import Http404, HttpResponse, JsonResponse
from upload_jason.models import JsonData

def index(request):
    branch = request.get_host().replace(".gutscheweb.com", "")

    if branch == "gutscheweb.com":
        return HttpResponse("Main page.........")

    if branch == "simconnect":
        list = JsonData.objects.values_list()
        result = {
            "data": [json.loads(entry[1]) for entry in list],
            "timestamps": [entry[2] for entry in list] 
        }
        return JsonResponse(result)
    
    else:
        raise Http404("Seite existiert nicht numbnuts")