from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.CharField(max_length=255, blank=False, null=False)
    price = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='static/images/products/')

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)
            output_size = (250, 250)
            img.thumbnail(output_size, Image.LANCZOS)
            img.save(self.image.path)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
