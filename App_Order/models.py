from django.db import models
from django.conf import settings
from App_Shop.models import Product
# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cart')
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=5)
    purchased=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'

    def get_total(self):
        total=self.item.price * self.quantity
        total=float(total)
        return format(total,'0.2f')

class Order(models.Model):
    order_items=models.ManyToManyField(Cart)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=300,blank=True,null=True)
    order_id=models.CharField(max_length=200,blank=True,null=True)

    def get_totals(self):
        total=0
        for order_item in self.order_items.all():
            total +=float(order_item.get_total())
        return total