from django.shortcuts import render,get_list_or_404,redirect,HttpResponse

from App_Order.models import Cart,Order
from App_Shop.models import Product

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

@login_required
def add_to_cart(request,pk):
    # return HttpResponse(pk)
    item=get_list_or_404(Product,pk=pk)
    order_item,created=Cart.objects.get_or_create(item=item,user=request.user,purchased=False)
    return HttpResponse(pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order=order_qs[0]
        if order.order_items.filter(item=item).exitst():
            order_item[0].quantity +=1
            order_item.save()
            messages.info(request,"This item quantity was updated")
            return redirect("App_shop:home")
        else:
            order.order_items.add(order_item[0])
            messages.info(request,'Item was added to your cart')
            return redirect("App_shop:home")
        
    else:
        order=Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request,"This item was added to your cart")
        return redirect("App_shop:home")
