from rest_framework.decorators import api_view
from rest_framework.response import Response
from myblog import models
from myblog.models import Classes, UserInfo
from myblog.toJson import Classes_data, UserInfo_data
import json

@api_view(['GET', 'POST'])
def  api_test(request):
    classes = Classes.objects.all()

    # classes_data = Classes_data(classes, many=True)
    #
    # userlist = UserInfo.objects.all()
    # # print(userlist.first())
    # userlist_data = UserInfo_data(userlist, many=True)
    # data = {
    #     'classes': classes_data.data,
    #     'userlist': userlist_data.data,
    # }
    data = {
        'classes': []
    }
    for c in classes:
        data_item = {
            'id': c.id,
            'text': c.text,
            'userlist': []
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                'id': user.id,
                'nickname':user.nickName,
                'headimg': str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    # data = json.dumps(data)
    return Response(data)
