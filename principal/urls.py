from django.urls import path
from .views import principal, delete

app_name = 'main'
urlpatterns = [
    path('', principal, name='entry'),
    path('<int:annotation_id>/', principal, name='change'),
    path('del/<int:annotation_id>/', delete, name='delete'),
]
