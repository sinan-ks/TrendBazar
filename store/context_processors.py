from django.db.models import Sum

def demo(request):
    return {"msg":"hello coder"}


def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        if request.user.cart.get_cart_items.count() > 0:
        # count = request.user.cart.cartitems.filter(is_order_placed=False).count()
           data = request.user.cart.cartitems.filter(is_order_placed=False).values_list('quantity').aggregate(total=Sum('quantity'))
           count = data.get('total')
    return {'item_count':count}