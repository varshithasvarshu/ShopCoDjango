from django.db import models

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.ForeignKey('product.Size', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.ForeignKey('product.Size', on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.cart.user.username
    