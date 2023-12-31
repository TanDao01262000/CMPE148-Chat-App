from django.urls import path
from . import views
from .views import open_new_room, rooms, room
app_name = 'room_app'

urlpatterns = [
    path("", views.rooms, name="rooms"),
    path("<str:room_name>", views.room, name="room"),
    path('open-new-room/', views.open_new_room, name='open_new_room'),
    path('delete/<int:room_id>/', views.delete_room, name='delete_room'),
]