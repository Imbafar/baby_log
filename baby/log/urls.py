from django.urls import path

from . import views

app_name = 'log'


urlpatterns = [
    path('', views.index, name='index'),
    path('2/', views.index2, name='index2'),
    
    path('create/', views.record_create, name='record_create'),
]
