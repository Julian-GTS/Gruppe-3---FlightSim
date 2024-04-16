from django.http import Http404
from django.shortcuts import render


def index(request):
    """
    Index view that serves requests only if they come from 'localhost'.
    """
    host = request.get_host().lower()  # Lowercase to handle any case variations
    allowed_domains = ["localhost", "127.0.0.1"]

    if any(host.startswith(domain) for domain in allowed_domains):
        return render(request, "index.html")
    else:
        raise Http404("This site is not accessible from your domain.")


def external(request):
    """
    A view to access the index page from any domain using '/external' path.
    """
    return render(request, "index.html")


def favicon(request):
    """
    Serves the favicon.ico from static files without needing to specify in HTML.
    """
    from django.conf import settings
    from django.http import FileResponse

    filepath = settings.BASE_DIR / "static" / "favicon.ico"
    return FileResponse(open(filepath, "rb"))


def robots(request):
    """
    Serves the robots.txt file to inform search engine crawlers about the site's policies.
    """
    from django.conf import settings
    from django.http import FileResponse

    filepath = settings.BASE_DIR / "static" / "robots.txt"
    return FileResponse(open(filepath, "rb"))
