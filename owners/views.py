from django.shortcuts import render
from .models import Virtual_Machine
# Create your views here.
def index(request):
    VM = Virtual_Machine.objects.all()
    return render(request, "index.html", {'owners' : VM})