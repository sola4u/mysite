from django.shortcuts import render,render_to_response
from django import forms
from django.http import Http404
from .models import *
import datetime

class Blog2(forms.Form):
    title = forms.CharField(max_length=32)
    author = forms.CharField(max_length=16)
    content = forms.CharField()
    catagory = forms.CharField() 
    tag = forms.CharField()
class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField()


def write_blogs(request):
    if request.method == 'POST':
        blog_form = Blog2(request.POST)
        if blog_form.is_valid():
            title = blog_form.cleaned_data['title']
            author = blog_form.cleaned_data['author']
            content = blog_form.cleaned_data['content']
#            created_date = blog_form.cleaned_data['created_date']
            catagory = blog_form.cleaned_data['catagory']
            tag = blog_form.cleaned_data['tag']
            cat = Catagory()
            cat.name = catagory
            cat.save()
            tag2 = Tag()
            tag2.name = tag
            tag2.save()
            blog = Blog.objects.create(title=title,author=author,content=content,catagory=cat)
            blog.save()
            blog.tag.add(tag2)
            return render_to_response("blog/editor.html",{'blog_form':blog_form,'msg':"发表成功"})
    else:
        blog_form = Blog2()
    return render_to_response('blog/editor.html',{'blog_form':blog_form})

def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created_date')
    return render_to_response('blog/blog_list.html',{'blogs':blogs})


def get_details(request,blog_id):
    try:
    	blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
    	raise Http404
    return render_to_response('blog/blog_details.html',{"blog":blog})
#    if request.method =='GET':
#        form = CommentForm()
#    else:
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            cleaned_data = form.cleaned_data
#            cleaned_data['blog'] = blog
#            Comment.objects.create(**cleaned_data)
#        ctx = {
#                'blog':blog,
#                'comments':blog.comment_set.all().order_by('-created_date'),
#                'form':form
#                }
#        return render(request,'blog_details.html',ctx)
