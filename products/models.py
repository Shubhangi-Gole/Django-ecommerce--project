from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
#
# from django.db import models
#
# class Product(models.Model):
#     CATEGORY_CHOICES = [
#         ('Electronics', 'Electronics'),
#         ('Fashion', 'Fashion'),
#         ('Accessories', 'Accessories'),
#     ]
#
#     name = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
#     image = models.ImageField(upload_to='products/')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
