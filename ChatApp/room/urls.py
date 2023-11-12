from django.urls import path
from . import views
app_name = 'room_app'

urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:name>", views.room, name="room"),
    
]