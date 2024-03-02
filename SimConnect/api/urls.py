from django.urls import path
from . import views

urlpatterns = [
    path("v1/", views.root, name="api-root"),
    path("v1/tree", views.tree, name="endpoint-list"),
]