from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Message

from .models import Room

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, room_name):
    try:
        room = get_object_or_404(Room, name=room_name)
        messages = Message.objects.filter(room=room)[:50]
        context = {
            'room': room,
            'messages':messages,
        }
        return render(request, 'room/room.html', context=context)
    except:
        return render(request, 'room/404.html')
    

# docker run --rm -p 6379:6379 redis:7