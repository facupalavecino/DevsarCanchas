from django.db import models
from django.utils import timezone


class Cancha(models.Model):
    """ Representación de una Cancha de fútbol """

    OPCIONES_TIPO_CANCHA = [
        ('C07', 'Cancha de 7'),
        ('C11', 'Cancha de 11')
    ]

    nombre = models.CharField(max_length=50, blank=False)
    codigo = models.CharField(unique=True, max_length=50, blank=False)
    tipo_cancha = models.CharField(
        max_length=3,
        choices=OPCIONES_TIPO_CANCHA,
        blank=True,
        default=""
    )
    tiene_vestuario = models.BooleanField(default=False)
    tiene_iluminacion = models.BooleanField(default=False)
    tiene_cesped_sintetico = models.BooleanField(default=False)


# class Empleado(models.Model):
#     """ Representación del Empleado del complejo """
#
#     nombre = models.CharField(max_length=35, blank=False)
#     apellido = models.CharField(max_length=35, blank=False)
#     dni = models.CharField(unique=True, max_length=8, blank=False)
#     fecha_nacimiento = models.DateField(blank=False, null=False)


class Reserva(models.Model):
    """ Representación de la Reserva de una cancha  """

    cliente = models.CharField(max_length=120, blank=False)
    empleado = models.CharField(max_length=120, blank=False)
    fecha_creacion = models.DateField(default=timezone.now, blank=False, null=False)
    fecha_reserva = models.DateTimeField(blank=False, null=False)
