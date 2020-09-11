from django.urls import path

from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.FieldsView.as_view(), name='canchas'),
    path('canchas', views.FieldsView.as_view(), name='canchas'),
    path('canchas/<int:pk>', views.FieldView.as_view(), name='cancha'),
    path('reservas/create', views.BookingCreateView.as_view(), name='create-reserva'),
    path('reservas/<int:pk>/delete', views.BookingDeleteView.as_view(), name='borrar-reserva'),
    path('reservas/<int:pk>/edit', views.BookingUpdateView.as_view(), name='editar-reserva')
]