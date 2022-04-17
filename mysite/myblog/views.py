from django.shortcuts import render, redirect
# from myblog.models import SiteInfo
from myblog import models


# Create your views here.

def index(request):
    # 基本信息
    siteinfo = models.SiteInfo.objects.all()[0]
    # 菜单分类
    classes = models.Classes.objects.all()
    # 全部用户
    userlist = models.UserInfo.objects.all()
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist,
    }
    return render(request, 'index.html', data)


# 测试是否可以合并1
# 测试是否可以合并2
# 测试3
def classes(request):
    # 基本信息
    global choose
    siteinfo = models.SiteInfo.objects.all()[0]
    # 菜单分类
    classes = models.Classes.objects.all()
    try:
        # 全部用户
        id = request.GET['id']
        choose = models.Classes.objects.filter(id=id)[0]
    except:
        return redirect('/')

    if choose:
        userlist = models.UserInfo.objects.filter(belong=choose)
    else:
        userlist = []
    data = {
        "siteinfo": siteinfo,
        "classes": classes,
        "userlist": userlist,
    }
    return render(request, 'classes.html', data)
