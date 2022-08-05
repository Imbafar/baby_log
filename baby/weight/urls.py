from django.urls import path

from . import views

app_name = "weight"


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.weight_create, name="weight_create"),
    path("amount/<int:weight_id>/edit/", views.weight_edit, name="weight_edit"),
    path("amount/<int:weight_id>/delete/", views.weight_delete, name="weight_delete"),
]
