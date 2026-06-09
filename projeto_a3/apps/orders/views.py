from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from orderitems.models import Orderitem
from games.models import Game
from players.models import Player
from supports.models import Support
from tickets.views import create_ticket_for_order

# Create your views here.
def list_orders(request):
    template_name = 'orders/list_orders.html'
    orders = Order.objects.select_related('player').all()
    context = {
        'orders': orders,
    }
    return render(request, template_name, context)


def list_items_games(request):
    template_name = 'orders/list_items_games.html'
    games = Game.objects.filter()
    context = {
        'games': games,
    }
    return render(request, template_name, context)


def cart(request):
    template_name = 'orders/cart.html'
    cart = request.session.get('cart', {})
    total = 0.0
    for key, item in cart.items():
        total += float(item['subtotal'])
    context = {
        'cart': cart,
        'total': total,
    }
    return render(request, template_name, context)


def add_cart(request, product_id):
    product = get_object_or_404(Game, id=product_id)
    cart = request.session.get('cart', {})
    pid = str(product.id)
    if pid in cart:
        cart[pid]['quantity'] += 1
    else:
        cart[pid] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'subtotal': float(product.price),
        }
    quantity = cart[pid]['quantity']
    price = float(cart[pid]['price'])
    cart[pid]['subtotal'] = price * quantity
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('orders:cart')


def edit_cart(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        pid = str(product_id)
        if pid in cart:
            if quantity <= 0:
                del cart[pid]
            else:
                price = float(cart[pid]['price'])
                cart[pid]['quantity'] = quantity
                cart[pid]['subtotal'] = price * quantity
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('orders:cart')


def delete_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('orders:cart')


def checkout(request):
    template_name = 'orders/checkout.html'
    cart = request.session.get('cart', {})
    total = 0.0
    for key, item in cart.items():
        total += float(item['subtotal'])
    players = Player.objects.all()
    supports = Support.objects.all()
    if request.method == 'POST':
        player_id = request.POST.get('player')
        # support_id = request.POST.get('support')
        payment_method = request.POST.get('payment_method')
        player = get_object_or_404(Player, id=player_id)
        # support = get_object_or_404(Support, id=support_id)
        order = Order.objects.create(
            player=player,
            # support=support,
            payment_method=payment_method,
            status='Finalizado',
            total=0
        )
        total_order = 0.0
        for product_id, item in cart.items():
            # product = get_object_or_404(Product, id=product_id)
            # quantity = int(item['quantity'])
            # unit_price = float(item['price'])
            subtotal = unit_price * quantity
            Orderitem.objects.create(
                order=order,
                # product=product,
                # quantity=quantity,
                # unit_price=unit_price,
                subtotal=subtotal
            )
            total_order += subtotal
        order.total = total_order
        order.save()
        create_ticket_for_order(order)
        request.session['cart'] = {}
        request.session.modified = True
        return redirect('orders:view_order', order_id=order.id)
    context = {
        'cart': cart,
        'total': total,
        'players': players,
        # 'supports': supports,
        'payment_methods': Order._meta.get_field('payment_method').choices,
    }
    return render(request, template_name, context)


def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.status != 'Cancelado':
        order.status = 'Cancelado'
        order.save()
    return redirect('orders:list_orders')


def view_order(request, order_id):
    template_name = 'orders/view_order.html'
    order = get_object_or_404(Order, id=order_id)
    items = order.items.all()
    context = {
        'order': order,
        'items': items,
    }
    return render(request, template_name, context)
