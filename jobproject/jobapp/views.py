from django.shortcuts import render
from .models import jobpost


# Create your views here.
def demo(request):
    obj = jobpost.objects.all()
    return render(request, "index.html", {'result': obj})
