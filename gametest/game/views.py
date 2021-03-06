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
           models.GUser.objects.filter(User_name=username, Password=password)
           # 插入新的用户数据
           return HttpResponse(json.dumps({'data': {'flag': True}}))
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
        mapid = request.POST.get("mapid", None)
        try:
            map = models.GMap.objects.filter(Map_ID=mapid)
            if map:
                return HttpResponse(json.dumps({'data': {'flag': True, 'map': {'mapContent': map.Content,
                                                         'date': map.Createtime,
                                                         'mapDescription': map.map_description}}}))
            else:
                return HttpResponse(json.dumps({'data': {'flag': False}}))
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))
@csrf_exempt
def getMap(mapid):
    try:
        map = models.GMap.objects.filter(Map_ID=mapid)
        if map:
            return map
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
def SaveMap(content, username, mapdescription=None, map_name=None):
    try:
        mapid = Hash(content)
        models.GMap.objects.create(Map_ID=mapid, Content=content, User_name=username, map_description=mapdescription,
                                   map_name=map_name)
        return mapid
    except:
        return 0

# 保存用户地图
@csrf_exempt
def AddMap(request):
    if request.method == "POST":
        content = request.POST.get("content", None)
        username = request.POST.get("username", None)
        mapdescription = request.POST.get("mapdescription", None)
        map_name = request.POST.get("map_name", None)
        try:
           mapid = SaveMap(content, username, mapdescription, map_name)
           return HttpResponse(json.dumps({'data': {'flag': False, 'mapid': mapid}}))
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
        stateid = request.POST.get("stateid", None)
        commentusername = request.POST.get("commentusername", None)
        content = request.POST.get("content", None)
        ismap = request.POST.get("IsMap", None)
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
        username = request.POST.get("username", None)
        content = request.POST.get("content", None)
        description = request.POST.get("feeling", None)
        statename = request.POST.get("statename", None)
        try:
            mapid = AddMap(content, username, description, statename)
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
            map = getMap(state_list.Map_ID)
            return HttpResponse(json.dumps({'data': {"flag": True, "state_list": state_list, "map_content": map.Content}}))

        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))
# 获取时间戳从高到低排序的动态列表
@csrf_exempt
def getNewState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-TimeStamp')
            map = getMap(state_list.Map_ID)
            return HttpResponse(json.dumps({'data': {"flag": True, "state_list": state_list, "map_content": map.Content}}))
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













