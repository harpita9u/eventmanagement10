from django.urls import path , include
from .import views

app_name = 'eventapp'

urlpatterns=[
    path('', views.projecthomepage, name='ProjectHomePage'),
    path('UserRegisterlogic/',views.UserRegisterlogic,name='UserRegisterlogic'),
    path('UserRegisterPagecall/',views.UserRegisterPagecall,name='UserRegisterPagecall'),
    path('add_event/',views.add_event,name='add_event'),
    path('event_list/',views.event_list,name='event_list'),

]