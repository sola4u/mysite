from rbac.models import UserInfo
from django.conf import settings

def nickname(request):
    try:
        return {'nickname':request.session['nickname'],
                'username':request.session['username'],
            }
    except:
        return {'nickname':'Stranger'}

def quanxian(request):
    try:
        return {'quanxian':request.session['quanxian']}
    except:
        return {'quanxian':None}
