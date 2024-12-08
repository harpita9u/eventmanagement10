from django.urls import path, include
from . import views
from .views import feedback_view, feedback_list

app_name = 'eventapp'

urlpatterns = [
    path('', views.projecthomepage, name='ProjectHomePage'),
    path('UserRegisterlogic/', views.UserRegisterlogic, name='UserRegisterlogic'),
    path('UserRegisterPagecall/', views.UserRegisterPagecall, name='UserRegisterPagecall'),
    path('add_event/', views.add_event, name='add_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path("about-us/", views.about_us, name="about_us"),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('about/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('faq/', views.faq_view, name='faq'),
    path('feedback/', feedback_view, name='feedback'),
    path('feedbacks/', feedback_list, name='feedback_list'),
]
