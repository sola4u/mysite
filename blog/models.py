#coding:utf8
from django.db import models
import django.utils.timezone as timezone
from markdownx.models import MarkdownxField
# Create your models here.

class Catagory(models.Model):
    name = models.CharField('catagory',max_length=30)

    def __str__(self): # def __unicode__(self): if python2
        return self.name

class Tag(models.Model):
    name = models.CharField('tag',max_length=16)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField('title',max_length=32)
    author = models.CharField('author',max_length=16)
    # author2 = models.CharField('author2',max_length=16)
    # content = models.TextField('content')
    content = MarkdownxField()
    created_date = models.DateTimeField('created_date',auto_now_add=True)
    catagory = models.ForeignKey(Catagory,verbose_name='catagory')
    tag = models.ManyToManyField(Tag,verbose_name='tag')

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,verbose_name='blog')
    name = models.CharField('name',max_length=16)
    email = models.EmailField('email')
    content = models.CharField('content',max_length=256)
    created_date = models.DateTimeField('post_time',auto_now_add=True)

    def __str__(self):
        return self.blog
