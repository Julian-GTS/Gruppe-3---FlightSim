from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_latest, name="api-redir-latest"),
    path("v1/", views.root, name="api-root"),
    path("v1/tree", views.tree, name="endpoint-list"),
    path("v1/serve-image", views.serve_image, name="serve-image"),
    path("v1/jsondata", views.jsondata, name="jsondata"),
]