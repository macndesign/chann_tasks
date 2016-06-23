from django.shortcuts import render
from channels import Channel

# Create your views here.
def home(request):
    msg = {}
    Channel('bg-hello').send(msg)
    Channel('bg-hello2').send(msg)
    return render(request, 'home.html', {})


def foo(request):
    msg = {}
    Channel('bg-foo').send(msg)
    return render(request, 'home.html', {})
