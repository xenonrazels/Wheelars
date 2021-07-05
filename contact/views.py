from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Inquery
from django.core.mail import send_mail
from django.urls import reverse_lazy
# Create your views here.
def inquery(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=request.POST['phone']
        email=request.POST['email']
        city=request.POST['city']
        car_title=request.POST['car_title']
        states=request.POST['state']
        car_id=request.POST['car_id']
        user_id=request.POST['user_id']
        customer_need=request.POST['customer_need']
        message=request.POST['message']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_inquired=Inquery.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_inquired:
                messages.error(request,"Sorry! you have already inquired about this product.Please, wait until we get back to you.")
                return redirect('cars:car_details', car_id)
        inquery=Inquery(car_id=car_id,first_name=first_name,last_name=last_name,phone=phone,car_title=car_title,email=email,city=city,state=states,user_id=user_id,customer_need=customer_need,message=message)
        inquery.save()
        messages.success(request,"Your inquery message is successfully sent ")
        send_mail(
        'New car inquery',
        "You have got a new inquery for the car"+ car_title +'.Please, login to your admin panel for more info.',
        'sudhanregmi25@gmail.com',
        ['jeevanregmi15@gmail.com'],
        fail_silently=False,
        )
        send_mail(
            'Inquery registered',
            "Hi,"+first_name+''+last_name+'\n' 'We have received your inquery for '+ car_title + 'We will contact you soon!..',
            'sudhanregmi25@gmail.com',
            [email],
            fail_silently=False,
        )

        return redirect('cars:car_details', car_id)
