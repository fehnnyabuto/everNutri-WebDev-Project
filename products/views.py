from django.shortcuts import render, redirect
from .forms import ProductForm
from django.http import HttpResponse
from .credentials import *
from .models import Product
from django.contrib import messages


def products(request):
    all_products = Product.objects.all()
    context = {"products": all_products}
    return render(request, 'products/shop.html', context)


def sell_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop-url')
    else:
        form = ProductForm()
    return render(request, 'products/sell.html', {'form': form})


def update_products(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        product_name = request.POST.get('name')
        product_quantity = request.POST.get('quantity')
        product_price = request.POST.get('price')
        product_description = request.POST.get('description')
        product_image = request.FILES.get('image')
        product.name = product_name
        product.quantity = product_quantity
        product.price = product_price
        product.description = product_description
        product.image = product_image
        product.save()
        messages.success(request, 'Product updated successfully')
        return redirect('shop-url')
    return render(request, 'products/update-products.html', {'product': product})


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully')
    return redirect('shop-url')


def checkout(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        phone = request.POST['phone']
        amount = product.price
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "PYMENT001",
            "TransactionDesc": "School fees"
        }

        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("success")
    return render(request, 'products/checkout.html', {'product': product})























#
# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'products/shop.html', {'products': products})











# @login_required
# def cart_detail(request):
#     cart_items = Cart.objects.filter(user=request.user)
#     total_price = sum(item.quantity * item.product.price for item in cart_items)
#
#     context = {
#         "cart_items": cart_items,
#         "total_price": total_price,
#     }
#
#     return render(request, "products/cart.html", context)

# def view_cart(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price})
#
#
# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     cart_item, created = CartItem.objects.get_or_create(product=product,
#                                                         user=request.user)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('cart:view_cart')
#
#
# def remove_from_cart(request, item_id):
#     cart_item = CartItem.objects.get(id=item_id)
#     cart_item.delete()
#     return redirect('cart:view_cart')


# most rec

# def add_to_cart(request, product_id):
#     product = Product.objects.get(pk=product_id)
#
#     # Check if the item is already in the cart
#     existing_item = CartItem.objects.filter(product=product).first()
#
#     if existing_item:
#         existing_item.quantity += 1
#         existing_item.save()
#     else:
#         CartItem.objects.create(product=product, quantity=1)
#
#     return redirect('cart-url')

#
# def cart(request):
#     cart_items = CartItem.objects.all()
#     total_price = sum(item.subtotal() for item in cart_items)
#     form = CartForm()
#
#     if request.method == 'POST':
#         form = CartForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             product_id = form.cleaned_data['product_id']
#             product = get_object_or_404(Product, pk=product_id)
#
#             cart_item, created = CartItem.objects.get_or_create(product=product)
#             cart_item.quantity += quantity
#             cart_item.save()
#             return redirect('cart')
#
#     return render(request, 'products/cart.html', {'cart_items': cart_items, 'total_price': total_price, 'form': form})


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/shop.html', context)


# def cart(request):
#     data = cartData(request)
#     cartItems = data['cartItems']
#     order = data['order']
#     items = data['items']
#
#     context = {'items': items, 'order': order}
#     return render(request, 'products/cart.html', context)


# def cart(request):
#
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#
#     context = {'items': items, 'order': order}
#     return render(request, 'products/cart.html', context)


# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#
#     print('Action:', action)
#     print('productId:', productId)
#
#     customer = request.user.customer
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#
#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity - 1)
#
#     orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#
#     return JsonResponse('Item was added', safe=False)


# def checkout(request):
#
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#
#     context = {'items': items, 'order': order}
#     return render(request, 'products/checkout.html', context)




# def checkout(request):
#     # Get the current user's cart items
#     cart_items = CartItem.objects.filter(user=request.user)
#
#     # Calculate the total price
#     total_price = sum(item.subtotal() for item in cart_items)
#
#     if request.method == 'POST':
#         # Assuming you have a form for the checkout details
#         # Create a form instance and populate it with data from the request
#         # You need to replace 'YourCheckoutForm' with the actual name of your checkout form
#         checkout_form = CheckoutForm(request.POST)
#
#         if checkout_form.is_valid():
#             # Process the checkout form data
#             # You can save the checkout details to your database or perform any other necessary actions
#
#             # Assuming you have a template for the 'thank you' page
#             return redirect('thank_you')
#
#     else:
#         # Assuming you have a form for the checkout details
#         # You need to replace 'YourCheckoutForm' with the actual name of your checkout form
#         checkout_form = CheckoutForm()
#
#     return render(request, 'products/checkout.html',
#                   {'cart_items': cart_items, 'total_price': total_price, 'checkout_form': checkout_form})


def thankyou(request):
    return render(request, 'products/thankyou.html')
