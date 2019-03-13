from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum

now = timezone.now()


def home(request):
    return render(request, 'rentadevapp/home.html',
                  {'rentadevapp': home})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form': form})

