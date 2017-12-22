from ..models import UserInfo, Menu

def init_permission(request, user_obj):
    permission_item_list = user_obj.roles.values('permissions__url',
                                                'permissions__title',
                                                'permissions__menu_id').distinct()
    permission_url_list = []
    permission_menu_list = []

    for item in permission_item_list:
        permission_url_list.append(item['permissions__url'])
        if item['permissions__menu_id']:
            temp = {'title':item['permissions__title'],
                    'url':item['permissions__url'],
                    'menu_id':item['permissions__menu_id']} 
            permission_menu_list.append(temp)

    menu_list = list(Menu.objects.values('id','title','parent_id'))
    
    from django.conf import settings

    request.session[settings.SESSION_PERMISSION_URL_KEY] = permission_url_list
    request.session[settings.SESSION_MENU_KEY] = {
            settings.ALL_MENU_KEY: menu_list,
            settings.PERMISSION_MENU_KEY:permission_menu_list,
        }


