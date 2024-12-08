from django import forms
from .models import EventList  # Make sure to import the EventList model

class EventForm(forms.ModelForm):
    class Meta:
        model = EventList
        fields = ['title', 'date', 'description']  # Adjust the fields as necessary
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Optional: to use a date input widget
        }
