from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('log.urls', namespace='logs')),
    path('about/', include('about.urls', namespace='about')),
    path('weight/', include('weight.urls', namespace='weight')),
    path('sleeptime/', include('sleeptime.urls', namespace='sleeptime')),
    path('admin/', admin.site.urls),
    
]
