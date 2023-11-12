from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, name):
    try:
        room = get_object_or_404(Room, name=name)
        return render(request, 'room/room.html', {'room': room})
    except:
        return render(request, 'room/404.html')
