from django.conf import settings
from django.http import FileResponse, Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from . import api_response, urls

def redirect_latest(request):
    return redirect("api-root")

def root(request):
    response = api_response.APIResponse(True, ["Welcome to the API!", "Endpoint list: /api/v1/tree"])
    return JsonResponse(response.to_json())

def tree(request):
    response = api_response.APIResponse(True, [pattern.name for pattern in urls.urlpatterns])
    return JsonResponse(response.to_json())
