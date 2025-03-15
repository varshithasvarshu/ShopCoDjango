from django.db import models

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.ForeignKey('product.Size', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
class Order_item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.ForeignKey('product.Size', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.order.user.username

class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_shipped = models.BooleanField(default=False)
    
    def __str__(self):
        return self.order.user.username