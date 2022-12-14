from django.urls import path

from . import views

app_name = "log"


urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.record_create, name="record_create"),
    path("records/<int:record_id>/", views.record_detail, name="record_detail"),
    path("records/<int:record_id>/edit/", views.record_edit, name="record_edit"),
    path("records/<int:record_id>/delete/", views.record_delete, name="record_delete"),
]
