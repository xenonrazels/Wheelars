from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contact.models import Inquery

# Create your views here.
def login(request):
    if request.method =='POST':
        email_username=request.POST['email_username']
        password=request.POST['Password']

        user =auth.authenticate(username=email_username, password=password)
        print(User.objects.values('id','username','password'))
        print(email_username)
        print(password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are logged in!!")
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Invalid User crediantials")
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    inquerys=Inquery.objects.all().filter(user_id= request.user.id)

    data={
        "inquerys":inquerys,
    }
    return render(request, 'accounts/dashboard.htm',data)

def register(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        conform_password=request.POST['confirm_password']
        if password==conform_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists.")
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"E-mail already exists.")
                    return redirect('accounts:register')
                else:

                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    messages.success(request,"You are logged in automatically")
                    auth.login(request,user=user)
                    return redirect('accounts:dashboard')
                    user.save()
                    messages.success(request,'You are registered successfully')
                    return redirect('accounts:login')

            return redirect('accounts:login')
        else:
            messages.error(request,"Password didn't match")
            return redirect('accounts:register')

    else:
        # messages.error(request,"form failes to submit")
        return render(request,'accounts/register.html')
def logout(request):
    auth.logout(request)
    return redirect('pages:home')