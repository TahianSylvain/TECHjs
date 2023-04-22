from tech_js import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls', namespace='main'))
]

# if settings.DEBUG:
#    urlpatterns += static.
