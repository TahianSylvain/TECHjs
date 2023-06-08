from django.urls import path, include
from rest_framework import routers
from .views import principal, delete, visiting,\
    listing_tasks_by_time
from .api_views import AnnotationViewSet, TaskViewSet, \
    _see_your_apis, _see_about_this_api


router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'annotation', AnnotationViewSet)


app_name = 'main'
urlpatterns = [
    path('', principal, name='entry'),

    path('api/', include(router.urls)),
    path('fullstack/', _see_your_apis, name='steward'),
    path('fullstack/<int:annotation_id>/', _see_about_this_api, name='steward'),

    path('journey/on<str:annotate_deadline_date>/', listing_tasks_by_time, name='on_this_day'),
    path('<int:annotation_id>/', principal, name='change'),
    path('foreign/<int:user_id>/', visiting, name='visiting'),
    path('del/<int:annotation_id>/', delete, name='delete'),
]
