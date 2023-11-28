from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    # if form is invalid return empty form
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('index.html')
    else:
        form = RegistrationForm()

    return render(request, 'auth/register.html', {"form": form})
