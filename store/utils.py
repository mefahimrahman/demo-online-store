import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('Cart: ', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items'] # Redundend for cart icon

    for productid in cart:
        try:
            cartItems += cart[productid]['quantity']

            product = Product.objects.get(id=productid)
            total = (product.price * cart[productid]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[productid]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[productid]['quantity'],
                'get_total': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True

        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}