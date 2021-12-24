from django import forms
# from django.contrib.auth import authenticate
from django.db.models import constraints
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate
from codes.forms import *
from user.models import *
from django.contrib.auth import authenticate, login,logout
from TwoFactor.utils import send_sms
# Create your views here.


@login_required
def home_view(request):
    return render(request,'main.html',locals())


def auth_view(request):
    form =AuthenticationForm()
    if request.method == "POST" :
        username=request.POST.get('username')
        password=request.POST.get('password')
        u = authenticate(request,username=username,password=password)
        if u is not None:
            request.session['pk']=u.pk
            user = CustomUser.objects.get(pk = u.pk)
            user.save()
            send_sms(user.code.number,user.phone_number)
            return redirect('verify-view')
        else:
            print("===")

    return render(request,'auth.html',{'form': form})


def verify_view(request):
    pk = request.session.get('pk')
    print(pk)
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        user = CustomUser.objects.get(pk = pk)
        print(user)
        if entered_otp == user.code.number:
            print("same")
            login(request,user)
            return redirect('home-view')

    return render(request,'verify.html')
