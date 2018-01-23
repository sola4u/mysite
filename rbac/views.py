#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import UserInfo as User
from django.template import RequestContext
from rbac.service.init_permission import init_permission
from django.conf import settings
# Create your views here.

class UserLogin(forms.Form):
    username = forms.CharField(label='username',max_length=50)
    password = forms.CharField(label='passwd',max_length=50)

class UserRegist(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    nickname = forms.CharField(label='nickname', max_length=32)
    password = forms.CharField(label='passwd', max_length=50)
    password2 = forms.CharField(label='passwd2', max_length=50)
    email = forms.EmailField(label='mail')

def regist(request):
    if request.method == 'POST':
        userform = UserRegist(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            userFilter = User.objects.filter(username=username)
            if userFilter:
                return render(request,'rbac/regist.html',{'userform':userform,'msg':'user exists'})
            else:
                password = userform.cleaned_data['password']
                password2 = userform.cleaned_data['password2']
                if (password != password2):
                    return render(request,'rbac/regist.html',{"userform":userform,'msg':"passwords dont match"})
                email = userform.cleaned_data['email']
                nickname = userform.cleaned_data['nickname']
                # gender = userform.cleaned_data['gender']
                user = User.objects.create(username=username,password=password,email=email,nickname=nickname)
                user.save()
                return render(request,'rbac/regist.html',{'msg':'create user successfully'})
    else:
        userform = UserRegist()
    return render(request,'rbac/regist.html',{'userform':userform})


def login(request):
    if request.method == 'POST':
        userform = UserLogin(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            userResult = User.objects.filter(username__exact=username, password__exact=password)
            if (len(userResult)>0):
                userResult2 = User.objects.get(username=username)
                request.session['member_id'] = userResult2.id
                request.session['username'] = userResult2.username
                request.session['nickname'] = userResult2.nickname
                init_permission(request, userResult2)
                #return render_to_response('rbac/index.html',{"msg":msg})
                permissions = userResult2.roles.values('permissions__url')
                permissions_list = []
                for i in permissions:
                    permissions_list.append(i['permissions__url'])
                quanxian = [
                {'title':'blog','urls':[['新建博客','/blog/write'],['查看博客','/blog/blog'],['本人博客','/blog/myblog']]},
                {'title':'accont','urls':[['新建用户','/rbac/regist'],['退出','/rbac/login']]},
                {'title':'abc','urls':[['退出','/rbac/logout']]}
                ]
                for i in quanxian:
                    for j in i['urls']:
                        if j[1] not in permissions_list:
                            i['urls'].remove(j)
                return render(request,'main.html',{"nickname":request.session['nickname'],
                                                   'quanxian':quanxian})
                # return render(request,'main.html')
            else:
                return render(request,'rbac/login.html',{"userform":userform,"msg":"用户名或密码错误！"})
    else:
        userform = UserLogin()
    return render(request,'rbac/login.html',{'userform':userform})
#    return render_to_response("rbac/login.html", {'username':username,'password':password})


def main(request):
    u = request.session.get('member_id')
    nickname = request.session.get('nickname')
    if u:
        return render(request,'main.html',{'nickname':nickname})
    else:
        return login(request)


def logout(request):
    try:
        # del request.session['member_id']
        request.session.clear()
    except KeyError:
        pass
   # return render_to_response("main.html",{'name':'Stranger'})
    return login(request)

def authorize(request):
    quanxian = [
    {'title':'blog','urls':['/blog/write','/blog/blog','/blog/myblog']},
    {'title':'accont','urls':['/rbac/regist','/rbac/login']}
    ]
    return render(request,'rbac/quanxian.html',{'quanxian':quanxian})
