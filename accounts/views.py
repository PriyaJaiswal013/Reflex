from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import *
from django.db.models import Sum, Q
import json
from decimal import Decimal
import binascii
import os
from django.conf import settings
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # username = email.split('@')[0]
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        mobile = request.POST.get('mobile')
        city = request.POST.get('city')
        landmark = request.POST.get('landmark')
        pin_code = request.POST.get('pin_code')
        address_first = request.POST.get('address_first')
        address = request.POST.get('address')
        restaurant_name = request.POST.get('restaurant_name')
        serving_type_food = request.POST.get('serving_type_food')
        fssai_number = request.POST.get('fssai_number')
        email = email.lower()
        cus = User.objects.filter(Q(email=email) | Q(username=email))
        # cus=User.objects.filter(username=username)
        if cus:
            messages.info(request, 'You are already exist.')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_staff = False
            user.is_active = True
            user.save()
            # key=binascii.hexlify(os.urandom(11)).decode()
            # request.user.userdetail.is_api_enabled = True
            # request.user.userdetail.save() 
            profileinfo = UserProfile(user=user, mobile=mobile, city=city, address_first=address_first,
                firstname=firstname,lastname=lastname, address=address, 
                restaurant_name=restaurant_name, serving_type_food=serving_type_food, 
                fssai_number=fssai_number, login_as=0, landmark=landmark, pin_code=pin_code)
            profileinfo.save()
             
            user = authenticate(username=email, password=password)
            # if user:
            #     login(request, user)
            return redirect('/')
    else:
        template_name = 'registration/signup.html'
        return render(request, template_name, { })

def cust_signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # username = email.split('@')[0]
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        mobile = request.POST.get('mobile')
        email = email.lower()
        cus = User.objects.filter(Q(email=email) | Q(username=email))
        if cus:
            messages.info(request, 'you are already exist.')
            
            return redirect('signup')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_staff = False
            user.is_active = True
            user.save()
            # key=binascii.hexlify(os.urandom(11)).decode()
            # request.user.userdetail.is_api_enabled = True
            # request.user.userdetail.save() 
            profileinfo = UserProfile(user=user, mobile=mobile,
                    firstname=firstname,lastname=lastname,login_as=1)
            profileinfo.save()
             
            user = authenticate(username=email, password=password)
            # if user:
            #     login(request, user)
            return redirect('/')
    else:
        template_name = 'registration/signup.html'
        return render(request, template_name, { })

def login_site(request):
    if request.method == "POST":
        cus = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = User.objects.get(username=username)
        except:
            try:
                cus = User.objects.get(email=username)
            except:
                return HttpResponseRedirect("/accounts/signin/?msg=Username is not correct.Please fill correct one.")
        user = authenticate(username=cus.username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/accounts/login/?msg=Password is not correct.Please fill correct one.")
    else:
        template_name = 'registration/login.html'
        return render(request, template_name, {})


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/accounts/login/")


def forgotpassword(request):
    template_name = 'registration/forgotpassword.html'
    msg = None
    if request.method == "POST":
        sourcemail = request.POST.get('email')
        username = request.POST.get('username')
        asd = str(sourcemail)
        try:
            obj = User.objects.get(email=asd, username=username)
            msg = "Please <a href='/accounts/login/%s/'>click here</a> for login on your account. After login please visit profile page to change your password for further use." % (
            obj.username)
        except Exception as e:
            return render(request, template_name,
                          {'msg': "We have not any user associated with that username and email id."})
        return render(request, template_name, {'msg': msg})
    return render(request, template_name, {})

@login_required
def accounts(request):
    template_name = 'registration/profile.html'
    if request.method == "POST":
        try:
            name = request.POST.get('first_name')
            mobile = request.POST.get('mobile')
            # skypeid = request.POST.get('skypeid')
            request.user.first_name = name
            request.user.save()
            request.user.userdetail.mobile = mobile
            # request.user.userdetail.skypeid = skypeid
            request.user.userdetail.save()
            return redirect('/')
        #     return HttpResponse(json.dumps(1), content_type="application/json")
        except:
            pass
        #     return HttpResponse(json.dumps(2), content_type="application/json")

    return render(request, template_name)

def changepassword(request):
    if not request.user.is_authenticated:
        return HttpResponse(json.dumps(3), content_type="application/json")
    password = request.POST.get('new_password')
    try:
        user = request.user
        user.set_password(password)
        user.save()
    except:
        return HttpResponse(json.dumps(2), content_type="application/json")

    return HttpResponse(json.dumps(1), content_type="application/json")
