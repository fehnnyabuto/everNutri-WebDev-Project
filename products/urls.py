from django.urls import path
from .views import sell_product
from . import views as my_views

urlpatterns = [
    path('', my_views.products, name='shop-url'),
    path('sell/', sell_product, name='sell-url'),
    path('delete/<id>', my_views.delete, name='delete-url'),
    path('update/<id>', my_views.update_products, name='update-url'),
    path('checkout/<id>', my_views.checkout, name='checkout-url'),
    path('thankyou/', my_views.thankyou, name='thankyou-url'),
]


