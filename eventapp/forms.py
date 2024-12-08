from django import forms
from .models import EventList  # Make sure to import the EventList model

class EventForm(forms.ModelForm):
    class Meta:
        model = EventList
        fields = ['title', 'date', 'description']  # Adjust the fields as necessary
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Optional: to use a date input widget
        }
from django import forms
from .models import Task
from .forms import *

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']

class UploadFileForm(forms.Form):
    file = forms.FileField()

# forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
