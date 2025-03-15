from django.db import models

# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    size = models.ForeignKey('product.Size', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username