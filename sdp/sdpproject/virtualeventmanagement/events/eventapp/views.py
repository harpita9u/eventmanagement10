from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render




# Create your views here.
def projecthomepage(request):
    return render(request, 'eventapp/ProjectHomePage.html')
from django.shortcuts import render, redirect
from .forms import EventForm
from .models import EventList  # Make sure to import the EventList model

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new event
            return redirect('event_list')  # Redirect to the event list view
    else:
        form = EventForm()  # Create a new empty form

    return render(request, 'eventapp/add_event.html', {'form': form})
def event_list(request):
    events = EventList.objects.all()  # Retrieve all events
    return render(request, 'eventapp/event_list.html', {'events': events})

def UserRegisterPagecall(request):
    return render(request, 'eventapp/UserRegisterPage.html')
def UserRegisterlogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'eventapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'eventapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'eventapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'eventapp/UserRegisterPage.html')
    else:
        return render(request, 'eventapp/UserRegister.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Render login page

# Logic for login
