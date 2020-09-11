from .models import Field, Booking
from django.forms import ModelForm

class BookingForm(ModelForm):
    """ Basic ModelForm for Booking objects """
    class Meta:
        model = Booking
        fields = ['field', 'client', 'employee', 'booked_at']
