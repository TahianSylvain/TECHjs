from app_users import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('switch_user/', views.user_logout, name='switch'),
    path('log_out/', views.user_logout, name='logout'),
    path('signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
]
