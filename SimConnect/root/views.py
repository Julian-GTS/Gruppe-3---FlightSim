import json
from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import redirect, render

def index(request):
    """
    Index gibt allen Anfragen auf root ("/") ein 404,
    außer die domäne ist simconnect.gutscheweb.com,
    gutscheweb.com oder www.gutscheweb.com. Bei den
    letzten zwei Optionen wird der klient per 302 auf
    die simconnect-subdomäne weitergeleitet.
    """
    host = request.get_host()

    allowed_domains = ["gutscheweb.com", "flightsense.tech"]

    domain = host.split(".")[-2] + "." + host.split(".")[-1]
    subdomain = host.split(".")[0] if len(host.split(".")) > 2 else None

    if subdomain == "www":
        return redirect("https://flightsense.tech")

    if domain in allowed_domains:
        return render(request, "index.html")
    
    else:
        raise Http404()

def external(request):
    """
    Um nun von einer anderen Domäne auf die index-seite
    zu gelangen, wird der "external"- path verwendet.
    Aufrufbar mit z.B. http://localhost/external.
    """
    return render(request, "index.html")


def favicon(request):
    """
    Der /favicon.ico-path wird standardmäßig von den
    gängigen Browsern abgerufen, ohne spezifikation im
    HTML.

    https://stackoverflow.com/questions/10218178/necessary-to-add-link-tag-for-favicon-ico
    """
    return FileResponse((settings.BASE_DIR / "static" / "favicon.ico").open("rb"))

def robots(request):
    """
    Der /robots.txt-path wird von Suchmaschinen-Crawlern
    abgerufen, um zu erfahren, welche Seiten indexiert
    werden dürfen und welche nicht.

    https://support.google.com/webmasters/answer/6062596?hl=de
    """
    return FileResponse((settings.BASE_DIR / "static" / "robots.txt").open("rb"))