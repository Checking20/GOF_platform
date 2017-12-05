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
                response = HttpResponse(json.dumps({'data': {'flag': True}}))
                response.set_cookie("username", username)
                return response
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
            response = HttpResponse(json.dumps({'data': {'flag': True}}))
            response.set_cookie("username", username)
            return response
        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))




# 根据Map_ID获取Map细节
@csrf_exempt
def getMapDetail(request):
    if request.method == "POST":
        mapid = request.POST.get("mapid")
        print(mapid)
        # mapid = 12341234
        try:
            mapp = models.GMap.objects.filter(Map_ID=mapid)
            if mapp:
                for maap in mapp:
                    re = maap.Content
                return HttpResponse(json.dumps({'data': {'flag': True, 'map': re}}))
            else:
                return HttpResponse(json.dumps({'data': {'flag': "jjj"}}))

        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))
@csrf_exempt
def getMap(mapid):
    try:
        mapp = models.GMap.objects.filter(Map_ID=mapid)
        if mapp:
            re = mapp
            return re
        else:
            return None
    except:
        return None

# Hash 生成Map_ID
#@csrf_exempt
def Hash(s):
    seed = 31
    mod = 1000000007
    hash = 0
    for i in range(len(s)):
        hash = (hash * seed + ord(s[i]) - ord('a') + 1) % mod
    print(hash)
    return hash

# 添加地图,返回地图ID
@csrf_exempt
def SaveMap(content, username):
    s = ''
    for i in range(len(content)):
        s = s + content[i]
    print(s)
    try:
        mapid = Hash(content)
        models.GMap.objects.create(Map_ID=mapid, Content=s, User_name=username)
        return mapid
    except:
        return 90

# 保存用户地图
@csrf_exempt
def AddMap(request):
    if request.method == "POST":
        content = request.POST.getlist('mapContent')
        #username = request.POST.get("username")
        #print(content)
        username = request.COOKIES["username"]
        #return HttpResponse(json.dumps({'data': {'username': content}}))
        try:
            mapid = SaveMap(content, username)
            #mapid = Hash(content)
            #print(mapid)
            #print(username)
            #models.GMap.objects.create(Map_ID=mapid, Content=content, User_name=username)
            if mapid != 90:
               return HttpResponse(json.dumps({'data': {'flag': True, 'mapid': mapid}}))
            else:
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
        stateid = request.POST.get("stateid")
        commentusername = request.COOKIES["username"]
        content = request.POST.get("content")
        try:
             models.Comment.objects.create(State_ID=stateid, Comment_User_name=commentusername, content=content)
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
            if state:
                for st in state:
                    temp1 = st
            else:
                return HttpResponse(json.dumps({'data': {'flag': False, 'state': None}}))
            comment = models.Comment.objects.filter(State_ID=stateid)
            if comment:
                for cc in comment:
                    temp2 = cc
            else:
                temp2 = None
            mapp = getMap(temp1.Map_ID)
            return HttpResponse(json.dumps({'data': {"flag": True, 'statedetail': {'state': temp1,
                                                                                   'map_content': mapp.Content,
                                                                                   'comment': temp2}}}))

        except:
            return HttpResponse(json.dumps({'data': {'flag': False}}))

# 发表新动态
@csrf_exempt
def AddState(request):
    if request.method == "POST":
        username = request.COOKIES["username"]
        content = request.POST.get("content")
        description = request.POST.get("description", None)
        statename = request.POST.get("statename", None)
        try:
            mapid = SaveMap(content, username)
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




#JFK  Here
@csrf_exempt
def getWorks(request):
    if request.method == "GET":
        type = request.GET.get("type")
        #热门
        if type == "hot":
            try:
                state_list = models.State.objects.all().order_by('-Like')
                mapp = getMap(state_list.Map_ID)
                return HttpResponse(
                    json.dumps({'data': {"flag": True, "state_list": state_list.id, "map_content": mapp.Content}}))
            except:
                return HttpResponse(json.dumps({'data': {'flag': False}}))
        #最近热门（待完成）
        if type == "recent_hot":
            #TODO LIST
            return HttpResponse(json.dumps({'data': {'flag': False}}))
        #最新
        if type == "lately":
            try:
                state_list = models.State.objects.all().order_by('-TimeStamp')
                mapp = getMap(state_list.Map_ID)
                return HttpResponse(
                    json.dumps({'data': {"flag": True, "state_list": state_list.id, "map_content": mapp.Content}}))
            except:
                return HttpResponse(json.dumps({'data': {'flag': False}}))
        #最早
        if type == "lastly":
            try:
                state_list = models.State.objects.all().order_by('TimeStamp')
                mapp = getMap(state_list.Map_ID)
                return HttpResponse(
                    json.dumps({'data': {"flag": True, "state_list": state_list.id, "map_content": mapp.Content}}))
            except:
                return HttpResponse(json.dumps({'data': {'flag': False}}))


def testhhh():
    mapid = 44587545
    username = "za"
    password = "123"
    # user = models.GMap.objects.filter(Map_ID=mapid)

    stateid = 2
    description = "hhh"
    statename = "bbb"
    content = "lihailihai"
    likenumber = 16
    # state = models.State.objects.filter(id=stateid)
    # models.State.objects.create(User_name=username, Map_ID=mapid, Description=description, State_name=statename)
    # models.Comment.objects.create(State_ID=stateid, Comment_User_name=username, content=content)
    # models.State.objects.filter(id=stateid).update(Like=likenumber)
    state_list = models.State.objects.all().order_by('-Like')
    mapp = getMap(state_list.Map_ID)
    state = models.Comment.objects.filter(State_ID=stateid)
    if mapp:
        for use in mapp:
            re = use
        return re
    else:
        return True
    # print(comment.Comment_User_name)


def test(request):
    abc = testhhh()
    return HttpResponse(json.dumps({'data': {'flag': abc.Content}}))



