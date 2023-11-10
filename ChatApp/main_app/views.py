from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def frontpage(request):
    return render(request, 'main_app/base.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            print('LOGIN')
            login(request, user)
            return redirect('room')
        else:
            messages.error(request, 'Username or password is incorrect!!')
    context = {}
    return render(request, 'main_app/login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {user}!')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')

    context = {'form': form}
    return render(request, 'main_app/signup.html', context)


def index(request):
    return render(request, "main_app/index.html")


# @login_required
def home(request):
    return render(request, 'main_app/index.html')

def room(request, room_name):
    return render(request, "main_app/room.html", {"room_name": room_name})

