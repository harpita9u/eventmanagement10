from django.urls import path
from . import views


app_name = 'userapp'

urlpatterns = [
    # Other URLs
    path('newuserpage/', views.NewUserPage, name='NewUserPage'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserLoginPagecall/', views.UserLoginPagecall, name='UserLoginPagecall'),
    path('logout/', views.UserLogout, name='UserLogout'),
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='event_list'),
]
