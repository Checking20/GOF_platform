from django.shortcuts import render
from django.shortcuts import HttpResponse
from game import models

# 登录
def login(request):
    have = False
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = models.GUser.objects.filter(User_name=username, Password=password)
        if user:
            have = True
        # 获取数据库内数据
    return render(request, "index.html", {"flag": have, "user": user})

# 注册新用户
def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        try:
           models.GUser.objects.create(User_name=username, Password=password)
           # 插入新的用户数据
           return render(request, "index.html", {"flag": True})
        except:
           return render(request, "index.html", {"flag": False})

# 根据State_ID获取Map
def getMap_byState_ID(stateid):
    try:
        mapid = models.State.objects.filter(id=stateid)
        map = models.GMap.objects.filter(Map_ID=mapid)
        return map
    except:
        return None
# 获取某个地图信息
def getMap(request):
    if request.method == "POST":
        mapid = request.POST.get("mapid", None)
        try:
            map = models.GMap.objects.filter(Map_ID=mapid)
            return render(request, "index.html", {"flag": True, "map": map})
        except:
            return render(request, "index.html", {"flag": False, "map": None})
# 保存用户地图
def SaveMap(request):
    if request.method == "POST":
        col = request.POST.get("col", None)
        row = request.POST.get("row", None)
        content = request.POST.get("content", None)
        username = request.POST.get("username", None)
        try:
           mapid = AddMap(col, row, content)
           models.GUser.objects.create(User_name=username, Map_ID=mapid)
           return render(request, "index.html", {"flag": True})
        except:
           return render(request, "index.html", {"flag": False})

# 添加地图,返回地图ID
def AddMap(col, row, content):
    try:
        mapid = Hash(content)
        models.GMap.objects.create(Map_ID=mapid, Col=col, Row=row, Content=content)
        return mapid
    except:
        return 0

# 返回State_ID数组的对应的Map内容
def getState_Map(State_List):
    pass

# mapid_list = models.State.objects.filter(id in State_List).values('Map_ID')
# map_list = models.GMap.objects.filter(Map_ID in mapid_list)
# return map_list

# 返回State_ID数组的对应的Comment内容
def getState_Comment(State_List):
    pass

# 返回动态
def getState(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        try:
            state = models.State.objects.filter(User_name=username)
            return render(request, "index.html", {"flag": True, "state": state})
        except:
            return render(request, "index.html", {"flag": False, "state": None})
# 发表新动态
def AddState(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        col = request.POST.get("col", None)
        row = request.POST.get("row", None)
        content = request.POST.get("content", None)
        feeling = request.POST.get("feeling", None)
        try:
           mapid = AddMap(col, row, content)
           if mapid != 0:
               models.State.objects.create(User_name=username, Map_ID=mapid, Feeling=feeling)
               return render(request, "index.html", {"flag": True})
           return render(request, "index.html", {"flag": False})
        except:
           return render(request, "index.html", {"flag": True})


# 发表评论，返回操作是否成功的状态
def AddComment(request):
    if request.method == "POST":
        stateid = request.POST.get("stateid", None)
        commentusername = request.POST.get("commentusername", None)
        content = request.POST.get("content", None)
        ismap = request.POST.get("ismap", None)
        try:
            models.Comment.objects.create(State_ID=stateid, Comment_User_name=commentusername, content=content, IsMap=ismap)
            return render(request, "index.html", {"flag": True})
        except:
            return render(request, "index.html", {"flag": False})

# 获取点赞量从高到低排序的动态列表
def getHotState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-Like')
            return render(request, "index.html", {"flag": True, "state_list": state_list})
        except:
            return render(request, "index.html", {"flag": False, "state_list": None})
# 获取时间戳从高到低排序的动态列表
def getNewState(request):
    if request.method == "POST":
        try:
            state_list = models.State.objects.all().order_by('-TimeStamp')
            return render(request, "index.html", {"flag": True, "state_list": state_list})
        except:
            return render(request, "index.html", {"flag": False, "state_list": None})















# Hash 生成Map_ID
def Hash(comment):
    seed = 31
    mod = 1000000007
    s = comment
    hash = 0
    for i in range(s.length()):
        hash = (hash * seed + s[i] - 'a' + 1) % mod
    return hash
