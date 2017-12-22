#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from .models import User
#from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.views.decorators.cache import cache_page
from django.template import RequestContext
# Create your views here.

#class UserForm(forms.Form):
#    username = forms.CharField(label='username', max_length=50)
#    password = forms.CharField(label='passwd', max_length=50)

class UserLogin(forms.Form):
    username = forms.CharField(label='username',max_length=50)
    password = forms.CharField(label='passwd',max_length=50)

class UserRegist(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    # gender = forms.CharField(label='gender', max_length=10)
    password = forms.CharField(label='passwd', max_length=50)
    password2 = forms.CharField(label='passwd2', max_length=50)
    email = forms.EmailField(label='mail')

@cache_page(60 * 15)
def regist(request):
    if request.method == 'POST':
        userform = UserRegist(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            userFilter = User.objects.filter(username=username)
            if userFilter:
                return render_to_response('users/regist.html',{'userform':userform,'msg':'user exists'})
            else:
                password = userform.cleaned_data['password']
                password2 = userform.cleaned_data['password2']
                if (password != password2):
                    return render_to_response('users/regist.html',{"userform":userform,'msg':"passwords dont match"})
                email = userform.cleaned_data['email']
                # gender = userform.cleaned_data['gender']
                user = User.objects.create(username=username,password=password,email=email)
                user.save()
                return render_to_response('users/regist.html',{'msg':'create user successfully'})
    else:
        userform = UserRegist()
    return render_to_response('users/regist.html',{'userform':userform})


def login(request):
    if request.method == 'POST':
        userform = UserLogin(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            userResult = User.objects.filter(username__exact=username, password__exact=password)
            if (len(userResult)>0):
                msg  = username + u'，登录成功！'
                #return render_to_response('users/index.html',{"msg":msg})
                #return render_to_response('main.html',{"name":username})
                return render(request,'main.html',{"name":username})
            else:
                return render_to_response('users/login.html',{"userform":userform,"msg":"用户名或密码错误！"})
    else:
        userform = UserLogin()
    return render_to_response('users/login.html',{'userform':userform})
#    return render_to_response("users/login.html", {'username':username,'password':password})


def index(request):
    return render_to_response("main.html",{'name':'Stranger'})
