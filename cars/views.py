from django.shortcuts import render

# Create your views here.
def car(request):
    return render(request,'pages/cars.html')