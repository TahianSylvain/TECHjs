from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import principal, delete, visiting,\
    listing_tasks_by_time, search_results, generated
from .api_views import AnnotationViewSet, TaskViewSet, \
    _see_your_apis, _see_about_this_api, UserCreate, LoginView


router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'annotation', AnnotationViewSet)


app_name = 'main'
urlpatterns = [
    path('', generated, name='generat'),  # principal, name='entry'),
    # path('generat/', generated, name='generat'),
    path('search/', search_results, name='search'),


    # path('api/', include(router.urls)),
    # path('login/', LoginView.as_view(), name='login'),
    # path('login/', obtain_auth_token, name='login'),
    # path('fullstack/', _see_your_apis, name='steward'),
    # path('signup/', UserCreate.as_view(), name='subscribe'),
    # path('fullstack/<int:annotation_id>/', _see_about_this_api, name='about_steward'),

    # path('journey/on<str:annotate_deadline_date>/', listing_tasks_by_time, name='on_this_day'),
    path('<int:annotation_id>/', principal, name='change'),
    path('foreign/<int:user_id>/', visiting, name='visiting'),
    path('del/<int:annotation_id>/', delete, name='delete'),
]
