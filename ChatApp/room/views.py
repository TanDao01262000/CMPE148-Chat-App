from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Message
from .forms import OpenNewRoom
from django.http import HttpResponse
from django.contrib import messages


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
@login_required
def open_new_room(request):
    if request.method == 'POST':
        form = OpenNewRoom(request.POST)
        if form.is_valid():
            room_name = form.cleaned_data['room_name']
            if not Room.objects.filter(name=room_name).exists():
                room = Room(name=room_name, created_by=request.user)
                room.save()
                return redirect('room_app:room', room_name=room_name)
            else:
                form.add_error('room_name', 'A room with this name already exists.')
    else:
            form = OpenNewRoom()

    return render(request, 'room/open_new_room.html', {'form': form})

@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    
    # Check if the user has permission to delete the room
    if request.user == room.created_by:
        room.delete()
        messages.success(request, f"Room '{room.name}' has been deleted successfully.")
    else:
        messages.error(request, "You don't have permission to delete this room.")
    
    return redirect('room_app:rooms')  # Redirect to the list of rooms
