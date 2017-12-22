from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r"^login/$", views.login),
    url(r"^regist/$", views.regist),
    url(r"^index/$", views.index),
    url(r"^logout/$", views.logout),
]

