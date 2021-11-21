from django.shortcuts import render
from home.models.orders import Order
def final(request):
   # id = Order.objects.only('id').get(name='kansas').id
    #print('order id is',Order.get_order_id())
    
    return render(request,'final.html')