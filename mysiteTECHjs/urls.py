from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls', namespace='main')),
    path('auth/', include('app_users.urls', namespace='app_user')),
]

# if settings.DEBUG:
#    urlpatterns += static.
