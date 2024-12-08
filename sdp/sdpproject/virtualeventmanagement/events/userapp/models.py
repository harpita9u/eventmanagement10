from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)  # Event title
    description = models.TextField()  # Event description
    date = models.DateField()  # Date of the event
    time = models.TimeField()  # Time of the event
    location = models.CharField(max_length=255)  # Location of the event

    def __str__(self):
        return self.title  # Return the event title for admin display
