from django.shortcuts import render, get_object_or_404
from tickets.models import Ticket

# Create your views here.
def create_ticket_for_order(order):
    if hasattr(order, 'ticket'):
        return order.ticket
    ticket_number = f'NF-{order.id:06d}'
    return Ticket.objects.create(
        order=order,
        number=ticket_number
    )

def view_ticket(request, ticket_id):
    template_name = 'tickets/view_ticket.html'
    ticket = get_object_or_404(ticket, id=ticket_id)
    context = {
        'ticket': ticket,
        'order': ticket.order,
        'items': ticket.order.items.all()
    }
    return render(request, template_name, context)
