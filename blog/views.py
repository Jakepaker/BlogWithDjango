from django.shortcuts import render
from .forms import Registration

# Create your views here.
def HomeView(request):
    context = {
        'title': 'Home',
        'name': 'James',
        'job': 'Web developer',
        'age': 18,
        'appeareance': 'handsome',
        'skills': ['HTML','CSS','Javascript','Python','Java','PHP']
    }
    return render(request, 'home.html', context=context)

def AboutView(request):
    return render(request, 'about.html')

def RegisterView(request):
    form = Registration()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST["password"]
        print(username, password)
        return render(request, 'register.html', {"form": form})
    return render(request, 'register.html', {'form': form})