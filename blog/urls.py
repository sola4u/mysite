from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r"^blog/$", views.get_blogs),
    url(r"^myblog/$", views.user_blogs),
    url(r"^write/$",views.write_blog),
    url(r'^edit$',views.edit_blog,name='bianji'),
    url(r'^detail/(\d+)/$',views.get_details,name="blog_get_detail"),
    url(r'^user_detail/(\d+)/$',views.user_details,name="user_get_detail"),
    url(r'^del/(\d+)/$',views.del_blog,name="blog_del"),
]
