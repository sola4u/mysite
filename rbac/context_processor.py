from rbac.models import UserInfo
from django.conf import settings

def nickname(request):
    return {'nickname':request.session['nickname'],'username':request.session['username']}
