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

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event, Registration  # Replace with your models

def register_event(request, event_id):
    # Get the event from the database
    event = get_object_or_404(Event, id=event_id)

    # Handle registration
    if request.method == 'POST':  # Ensure it's a form submission
        # Assume a Registration model links the user to an event
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to register.")
            return redirect('login')  # Redirect to login page if not authenticated

        # Check if the user has already registered
        if Registration.objects.filter(event=event, user=request.user).exists():
            messages.warning(request, "You have already registered for this event.")
        else:
            Registration.objects.create(event=event, user=request.user)
            messages.success(request, f"Successfully registered for {event.title}!")

        return redirect('event_list')  # Replace with your desired redirect page

    # Optionally, render a registration confirmation page
    return render(request, 'event/register.html', {'event': event})


from django.shortcuts import render
from .models import Event

def event_list(request):
    # Fetch all events from the database
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})

from django.shortcuts import render

def about_us(request):
    return render(request, "about_us.html")

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
def add_task(request):
    if request.method == 'POST':  # Corrected methods to method
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventapp:add_task')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'eventapp/add_task.html', {'form': form, 'tasks': tasks})  # Added comma after request

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)  # Fixed typo from get_object_or_484 to get_object_or_404
    task.delete()
    return redirect('eventapp:add_task')

from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO #Use BytesIO for binary data
import base64
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x-1])

        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%')
        plt.title('Sales Distribution per Month')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'eventapp/chart.html', {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })
    return render(request, 'eventapp/chart.html', {'form':UploadFileForm()})

# myapp/views.py
from django.shortcuts import render

def about_us(request):
    return render(request, 'eventapp/about_us.html')

from django.shortcuts import render

def contact_us(request):
    return render(request, 'eventapp/contact_us.html')

# Render login page

# Logic for login
from django.shortcuts import render
from .models import FAQ

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'eventapp/faq.html', {'faqs': faqs})

# views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'eventapp/feedback_success.html')  # Display a thank-you message
    else:
        form = FeedbackForm()
    return render(request, 'eventapp/feedback.html', {'form': form})

# views.py
from django.shortcuts import render
from .models import Feedback

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'eventapp/feedback_list.html', {'feedbacks': feedbacks})
