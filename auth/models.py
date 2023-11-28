from django.db import models

# Create your models here.

# muindi
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.db import models
# from django.db.models.signals import post_save
#
# from products.models import Product
#
#
# User = get_user_model()
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)
#     products = models.ManyToManyField(Product, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# def post_save_profile_create(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.get_or_create(user=instance)
#
#
# post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
