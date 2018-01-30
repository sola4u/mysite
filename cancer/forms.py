#coding:utf-8

from django.forms import ModelForm
from .models import Cancer

class Patient(ModelForm):
    class Meta:
        model = Cancer
        fields = "__all__"
