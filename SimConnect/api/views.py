from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from . import urls

def root(request):
    return HttpResponse("api :)")

def tree(request):
    return HttpResponse("bald")
    # patterns = []
    # for pattern in urls.urlpatterns:
    #     print("a")
    #     patterns.append(pattern.name)
    
    # return JsonResponse(patterns)