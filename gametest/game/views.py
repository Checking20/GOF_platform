from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

# Create your views here.
# 登录
@csrf_exempt
def index(request):
    return render(request, "index.html")
@csrf_exempt
def share(request):
    return render(request, "share.html")
@csrf_exempt
def begin(request):
    return render(request, "begin.html")
@csrf_exempt
def work(request):
    return render(request, "work.html")

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = models.GUser.objects.filter(User_name=username, Password=password)
            # 插入新的用户数据
            if user:
               return HttpResponse(json.dumps({'data': {'flag': True}}))
            else:
               return HttpResponse(json.dumps({'data': {'flag': False}}))
        except:
               return HttpResponse(json.dumps({'data': {'flag': False}}))

# 注册新用户

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
           models.GUser.objects.create(User_name=username, Password=password)
           # 插入新的用户数据
           return HttpResponse(json.dumps({'data': {'flag': True}}))
        except:
           return HttpResponse(json.dumps({'data': {'flag': False}}))




# 根据Map_ID获取Map细节
@csrf_exempt
def getMapDetail(request):
    if request.method == "POST":
        mapid = request.POST.get("mapid")
        try:
            mapp = models.GMap.objects.filter(Map_ID=mapid)
            if mapp:
                return HttpResponse(json.dumps({'data': {'flag': True, 'map': mapp}}))
            else:
                return HttpResponse(json.dumps({'data': {'flag': False}}))

        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))
@csrf_exempt
def getMap(mapid):
    try:
        mapp = models.GMap.objects.filter(Map_ID=mapid)
        if mapp:
            return mapp
        else:
            return None
    except:
        return None

# Hash 生成Map_ID
@csrf_exempt
def Hash(comment):
    seed = 31
    mod = 1000000007
    s = comment
    hash = 0
    for i in range(s.length()):
        hash = (hash * seed + s[i] - 'a' + 1) % mod
    return hash

# 添加地图,返回地图ID
@csrf_exempt
def SaveMap(content, username):
    try:
        mapid = Hash(content)
        models.GMap.objects.create(Map_ID=mapid, Content=content, User_name=username)
        return mapid
    except:
        return 90

# 保存用户地图
@csrf_exempt
def AddMap(request):
    if request.method == "POST":
        content = request.POST.get("content")
        username = request.POST.get("username")
        try:
            mapid = SaveMap(content, username)
            if mapid != 90:
               return HttpResponse(json.dumps({'data': {'flag': True, 'mapid': mapid}}))
            else:
               return HttpResponse(json.dumps({'data': {'flag': False}}))

        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))

# 获取一个用户保存的所有地图
@csrf_exempt
def getAllMap(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        try:
            map = models.GMap.objects.filter(User_name=username)
            if map:
                return HttpResponse(json.dumps({'data': {'flag': False, 'map_content': map.Content}}))
            else:
                return HttpResponse(json.dumps({'data': {'flag': False}}))
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))

# 发表评论，返回操作是否成功的状态
@csrf_exempt
def AddComment(request):
    if request.method == "POST":
        stateid = request.POST.get("stateid")
        commentusername = request.POST.get("commentusername")
        content = request.POST.get("content", None)
        ismap = request.POST.get("IsMap")
        try:
             models.Comment.objects.create(State_ID=stateid, Comment_User_name=commentusername, content=content,
                                           IsMap=ismap)
             return HttpResponse(json.dumps({'data': {'flag': True}}))
        except:
             return HttpResponse(json.dumps({'data': {'flag': False}}))


# 返回动态
@csrf_exempt
def getStateDetail(request):
    if request.method == "POST":
        stateid = request.POST.get("stateid", None)
        try:
            state = models.State.objects.filter(id=stateid)
            comment = models.Comment.objects.filter(State_ID=stateid)
            map = getMap(state.Map_ID)
            if state & map:
               return HttpResponse(json.dumps({'data': {"flag": True, 'statedetail': {"state": state, "map_content": map.Content,
                                                        "comment": comment}}}))
            else:
               return HttpResponse(json.dumps({'data': {'flag': False}}))
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))

# 发表新动态
@csrf_exempt
def AddState(request):
    if request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        description = request.POST.get("feeling", None)
        statename = request.POST.get("statename", None)
        try:
            mapid = SaveMap(content, username, description, statename)
            if mapid != 0:
               models.State.objects.create(User_name=username, Map_ID=mapid, Description=description,
                                           State_name=statename)
               return HttpResponse(json.dumps({'data': {'flag': True}}))
            else:
               return HttpResponse(json.dumps({'data': {'flag': False}}))
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))



# 获取点赞量从高到低排序的动态列表
@csrf_exempt
def getHotState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-Like')
            mapp = getMap(state_list.Map_ID)
            return HttpResponse(json.dumps({'data': {"flag": True, "state_list": state_list, "map_content": mapp.Content}}))

        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))
# 获取时间戳从高到低排序的动态列表
@csrf_exempt
def getNewState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-TimeStamp')
            mapp = getMap(state_list.Map_ID)
            return HttpResponse(json.dumps({'data': {"flag": True, "state_list": state_list, "map_content": mapp.Content}}))
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))

# 更新点赞数
@csrf_exempt
def AddLike(request):
    if request.method == "POST":
        stateid = request.POST.get("stateid")
        likenumber = request.POST.get("like")
        try:
            models.State.objects.filter(id=stateid).update(Like=likenumber)
            return HttpResponse(json.dumps({'data': {'flag': True}}))
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))













