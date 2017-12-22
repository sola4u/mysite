from rbac.models import UserInfo
from django.conf import settings

def nickname(request):
    a = UserInfo.objects.get(username=settings.USERNAME)
    return {'nickname':a.nickname}
