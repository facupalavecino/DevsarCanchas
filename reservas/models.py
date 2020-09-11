from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Field(models.Model):
    """ Represents a soccer field """

    FIELD_TYPE_CHOICES = [
        ('C05', 'Cancha de 5'),
        ('C07', 'Cancha de 7'),
        ('C11', 'Cancha de 11')
    ]

    name = models.CharField(max_length=50, blank=False)
    code = models.CharField(unique=True, max_length=50, blank=False)
    field_type = models.CharField(
        max_length=3,
        choices=FIELD_TYPE_CHOICES,
        blank=True,
        default=""
    )
    has_locker = models.BooleanField(default=False)
    has_light = models.BooleanField(default=False)
    has_synthetic_grass = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """ Represents a field reservation """

    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="booked_field", null=False, blank=False)
    client = models.CharField(max_length=120, blank=False)
    employee = models.CharField(max_length=120, blank=False)
    created_at = models.DateField(default=timezone.now, blank=False, null=False)
    booked_at = models.DateTimeField(blank=False, null=False)

    class Meta:
        unique_together = ['field', 'booked_at']

    def clean(self):
        """ Validates that the booking does not overlap with an existing one """
        overlapped_bookings = Booking.objects.filter(
            Q(booked_at__gt=self.booked_at - timedelta(hours=1), booked_at__lte=self.booked_at)
            |
            Q(booked_at__gte=self.booked_at, booked_at__lt=self.booked_at + timedelta(hours=1))
        )
        if overlapped_bookings.count() > 0:
            raise ValidationError(f"La reserva se sobrepone con otra ya existente")

    def __str__(self):
        return f'Reserva en "{str(self.field)}", a las {str(self.booked_at)}'

    def formatted_date(self):
        """ Returns the creation date formatted """
        return f'{self.created_at.strftime("%d/%m/%Y")}'

    def formatted_datetime(self):
        """ Returns the booking datetime formatted """
        return f'{self.booked_at.strftime("%d/%m/%Y - %H:%M")}'
