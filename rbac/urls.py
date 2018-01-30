from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^login/$", views.login),
    url(r"^regist/$", views.regist),
    url(r"^logout/$", views.logout),
    url(r"^quanxian/$", views.authorize),
    url(r"^user_edit/$", views.user_edit),
]
