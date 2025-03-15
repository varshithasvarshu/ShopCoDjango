from django.db import models

# Create your models here.
class ProductReview(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.user.username