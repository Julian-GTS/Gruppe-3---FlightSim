import json
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render

def index(request):
    branch = request.get_host().replace(".gutscheweb.com", "")

    if branch == "gutscheweb.com" or branch == "www":
        return redirect("https://simconnect.gutscheweb.com")

    if branch == "simconnect":
        return render(request, "index.html")
    
    else:
        raise Http404()
    
def favicon(request):
    return FileResponse((settings.BASE_DIR / "static" / "favicon.ico").open("rb"))