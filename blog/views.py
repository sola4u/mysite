from django.shortcuts import render,render_to_response,redirect
from django import forms
from django.http import Http404,HttpResponse
from .models import *
from markdownx.fields import MarkdownxFormField
import datetime
from rbac.models import UserInfo
from django.conf import settings

class Blog2(forms.Form):
    title = forms.CharField(max_length=32)
    # author = forms.CharField(max_length=16)
    # content = forms.CharField()
    content = MarkdownxFormField()
    catagory = forms.CharField()
    tag = forms.CharField()
class CommentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField()

def write_blog(request):
    if request.method == 'POST':
        blog_form = Blog2(request.POST)
        if blog_form.is_valid():
            title = blog_form.cleaned_data['title']
            content = blog_form.cleaned_data['content']
            content = content.replace('<script>','&lt;script&gt;').replace('</script>','&lt;/script&gt;')
            author = request.session['nickname']
            # author2 = request.session['nickname']
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
            get_blogs(request)
            blogs = Blog.objects.all().order_by('-created_date')
            return render(request,'blog/blog_list.html',{'blogs':blogs,'blog_detail':"blog_get_detail"})
            # return render_to_response("blog/write.html",{'blog_form':blog_form,'msg':"发表成功"})
    else:
        blog_form = Blog2()
    return render_to_response('blog/write.html',{'blog_form':blog_form})

def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created_date')
    return render_to_response('blog/blog_list.html',{'blogs':blogs,'blog_detail':"blog_get_detail"})

def get_details(request,blog_id):
    try:
    	blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
    	raise Http404
    blogs = Blog.objects.all().order_by('-id')
    id_list = []
    for i in blogs:
        id_list.append(i.id)
    blog_id = int(blog_id)
    this_id = id_list.index(int(blog_id))
    try:
        pre_blog_id = id_list[this_id + 1]
    except IndexError:
        pre_blog_id = id_list[-1]
    try:
        next_blog_id = id_list[this_id - 1]
    except IndexError:
        next_blog_id = id_list[0]
    pre_blog_title = Blog.objects.get(id=pre_blog_id).title
    next_blog_title = Blog.objects.get(id=next_blog_id).title
    return render_to_response('blog/blog_details.html',{"blog":blog,'pre_blog_id':pre_blog_id,
                                'next_blog_id':next_blog_id,  'pre_blog_title':pre_blog_title,
                                'next_blog_title':next_blog_title,'blog_detail':"blog_get_detail"
                            })
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

def edit_blog(request):
    # forerurl = '/'.join(request.path.split('/')[:-2])
    # return redirect(formerurl)
    if request.method == "GET":
        nid = request.GET.get('nid')
        blog = Blog.objects.filter(pk=nid).first()
        return render(request,'blog/editor.html',{'blog':blog})
    elif request.method == 'POST':
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        content = request.POST.get('content')
        content = content.replace('<script>','&lt;script&gt;').replace('</script>','&lt;/script&gt;')
        Blog.objects.filter(pk=nid).update(title=title,content=content)
        blogs = Blog.objects.all().order_by('-created_date')
        return render(request,'blog/blog_list.html',{'blogs':blogs,'blog_detail':"blog_get_detail"})


def del_blog(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.session['nickname'] == blog.author:
        blog.delete()
        msg = '删除成功'
        blogs = Blog.objects.all().order_by('-created_date')
        return render(request,'blog/blog_list.html',{'blogs':blogs,'msg':msg,'blog_detail':"user_get_detail"})
    else:
        msg = '无权限删除'
        blogs = Blog.objects.all().order_by('-created_date')
        return render(request,'blog/blog_list.html',{'blogs':blogs, 'msg':msg,'blog_detail':"blog_get_detail"})

def user_blogs(request):
    author = request.session['nickname']
    blogs = Blog.objects.filter(author=author).order_by('-id')
    return render_to_response('blog/blog_list.html',{"blogs":blogs,'blog_detail':"user_get_detail"})

def user_details(request,blog_id):
    author = request.session['nickname']
    try:
    	blog = Blog.objects.filter(author=author).get(id=blog_id)
    except Blog.DoesNotExist:
    	raise Http404
    blogs = Blog.objects.filter(author=author).order_by('-id')
    id_list = []
    for i in blogs:
        id_list.append(i.id)
    print(id_list)
    blog_id = int(blog_id)
    this_id = id_list.index(int(blog_id))
    try:
        pre_blog_id = id_list[this_id + 1]
    except IndexError:
        pre_blog_id = id_list[-1]
    try:
        next_blog_id = id_list[this_id - 1]
    except IndexError:
        next_blog_id = id_list[0]
    pre_blog_title = Blog.objects.get(id=pre_blog_id).title
    next_blog_title = Blog.objects.get(id=next_blog_id).title
    return render_to_response('blog/blog_details.html',{"blog":blog,'pre_blog_id':pre_blog_id,
                                'next_blog_id':next_blog_id,  'pre_blog_title':pre_blog_title,
                                'next_blog_title':next_blog_title,'blog_detail':"user_get_detail"
                            })
