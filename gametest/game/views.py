from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

# Create your views here.
# 登录
def index(request):
    return render(request, "index.html")

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
           user = models.GUser.objects.get(User_name=username, Password=password)
           if user != None:
               return HttpResponse(json.dumps({'data': {'flag': True, 'user': user}}))
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
def getMapDetail(request):
    if request.method == "POST":
        mapid = request.POST.get("mapid", None)
        try:
            map = models.GMap.objects.get(Map_ID=mapid)
            if map:
                return render(request, "index.html", {"flag": True, "map": map})
            else:
                return render(request, "index.html", {"flag": False})
        except:
            return render(request, "index.html", {"flag": False})

def getMap(mapid):
    try:
        map = models.GMap.objects.get(Map_ID=mapid)
        if map:
            return map
        else:
            return None
    except:
        return None

# Hash 生成Map_ID
def Hash(comment):
    seed = 31
    mod = 1000000007
    s = comment
    hash = 0
    for i in range(s.length()):
        hash = (hash * seed + s[i] - 'a' + 1) % mod
    return hash

# 添加地图,返回地图ID
def AddMap(content, username, mapdescription=None, map_name=None):
    try:
        mapid = Hash(content)
        models.GMap.objects.create(Map_ID=mapid, Content=content, User_name=username, map_description=mapdescription,
                                   map_name=map_name)
        return mapid
    except:
        return 0

# 保存用户地图
def SaveMap(request):
    if request.method == "POST":
        content = request.POST.get("content", None)
        username = request.POST.get("username", None)
        mapdescription = request.POST.get("mapdescription", None)
        map_name = request.POST.get("map_name", None)
        try:
           mapid = AddMap(content, username, mapdescription, map_name)
           return render(request, "index.html", {"flag": True, "mapid": mapid})
        except:
           return render(request, "index.html", {"flag": False})

# 获取一个用户保存的所有地图
def getAllMap(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        try:
            map = models.GMap.objects.get(User_name=username)
            if map:
                return render(request, "index.html", {"flag": True, "map": map})
            else:
                return render(request, "index.html", {"flag": False})
        except:
            return render(request, "index.html", {"flag": False})

# 发表评论，返回操作是否成功的状态
def AddComment(request):
    if request.method == "POST":
        stateid = request.POST.get("stateid", None)
        commentusername = request.POST.get("commentusername", None)
        content = request.POST.get("content", None)
        ismap = request.POST.get("IsMap", None)
        try:
             models.Comment.objects.create(State_ID=stateid, Comment_User_name=commentusername, content=content,
                                           IsMap=ismap)
             return render(request, "index.html", {"flag": True})
        except:
             return render(request, "index.html", {"flag": False})


# 返回动态
def getStateDetail(request):
    if request.method == "POST":
        stateid = request.POST.get("stateid", None)
        try:
            state = models.State.objects.get(id=stateid)
            comment = models.Comment.objects.get(State_ID=stateid)
            map = getMap(state.Map_ID)
            if state & map:
               return render(request, "index.html", {"flag": True, "state": state, "map": map.Content,
                                                     "comment": comment})
            else:
               return render(request, "index.html", {"flag": False})
        except:
            return render(request, "index.html", {"flag": False})

# 发表新动态
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
               return render(request, "index.html", {"flag": True})
            else:
               return render(request, "index.html", {"flag": False})
        except:
            return render(request, "index.html", {"flag": False})



# 获取点赞量从高到低排序的动态列表
def getHotState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-Like')
            map = getMap(state_list.Map_ID)
            return render(request, "index.html", {"flag": True, "state_list": state_list.id, "map": map.Content})
        except:
            return render(request, "index.html", {"flag": False, "state_list": None})
# 获取时间戳从高到低排序的动态列表
def getNewState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-TimeStamp')
            return render(request, "index.html", {"flag": True, "state_list": state_list.id, "map": map.Content})
        except:
            return render(request, "index.html", {"flag": False, "state_list": None})


# 点赞数
def AddLike(request):
    if request.method == "POST":
        pass












