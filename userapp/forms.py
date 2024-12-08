from django import forms
from .models import Event  # Import the Event model

class EventForm(forms.ModelForm):
    class Meta:
        model = Event  # Specify the model to use
        fields = ['title', 'description', 'date', 'time', 'location']  # Fields to include in the form
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Customize the description field
            'date': forms.SelectDateWidget(),  # Use a date picker for the date field
        }
