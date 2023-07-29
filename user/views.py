from django.shortcuts import render
from .forms import Registration
from django.contrib.auth.models import User

# Create your views here.
def RegisterView(request):
    form = Registration(request.POST)
    if form.is_valid():
        cleaned_form = form.clean()
        User.objects.create(**cleaned_form)
        return render(request, 'home.html')
    return render(request, 'register.html', {'form': form})

def LoginView(request):
    pass