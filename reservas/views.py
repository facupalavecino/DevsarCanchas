from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models.query import EmptyQuerySet

from .forms import BookingForm
from .models import Field, Booking


class FieldsView(generic.ListView):
    """ Class view for a list of fields """
    template_name = 'reservas/fields.html'
    context_object_name = 'field_list'

    def get_queryset(self):
        """ Returns all the Fields registered """
        return Field.objects.all()


class FieldView(generic.DetailView):
    """ Class view for a single field """
    model = Field
    template_name = 'reservas/field_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservas'] = Booking.objects.filter(field=self.get_object()).order_by('-created_at')[:20]
        return context


class BookingDeleteView(generic.DeleteView):
    model = Booking
    template_name = 'reservas/delete_booking.html'
    success_url = reverse_lazy('reservas:canchas')


class BookingUpdateView(generic.UpdateView):
    """ Generic view that renders a pre-populated form to update a Booking instance """
    model = Booking
    form_class = BookingForm
    template_name = 'reservas/edit_booking_form.html'

    def form_valid(self, form):
        f = form.save()
        return HttpResponseRedirect(f'../../canchas/{f.field.id}')


class BookingCreateView(generic.CreateView):
    """ Generic view that renders an empty form to create a Booking instance """
    model = Booking
    form_class = BookingForm
    template_name = 'reservas/create_booking_form.html'

    def form_valid(self, form):
        f = form.save()
        return HttpResponseRedirect(f'../canchas/{f.field.id}')
