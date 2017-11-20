/**
 * author:zq
 * time:2017/11/20
 * 加载当前展示作品
 * 加载作品所属用户信息
 * 加载当前作品所有的评论
 * 给当前作品添加评论
 */


 //一个map要有所属用户  还有相关评论的所属用户
(function(){
    // manager
    var manager = {
        mapId,//当前作品的id
        init:function(mapId){
            manager.mapId = mapId;
            $.ajax({
                type: "POST",
                url: "/getMap",
                data: { "mapId":mapId },
                dataType: 'json',
                success: function (myData) {
                   //加载作品页面逻辑
                   user.name = myData.data.name;
                   user.avatar = myData.data.avatar;
                },
                error: function (xhr, type) {
                    console.log(type);
                },
            });
        },
        getComments:function(mapId){ //得到评论
            $.ajax({
                type: "POST",
                url: "/getComments",
                data: { "mapId":mapId },
                dataType: 'json',
                success: function (myData) {
                   work.comments = myData.data.comments;//数组不能直接赋值
                },
                error: function (xhr, type) {
                    console.log(type);
                },
            });
        },
    }
    // 作品所属用户
    var user = {
        name,
        avatar,
    }
    // 当前界面的唯一作品
    var work = {
        user:user, //作品所属用户
        comments:[], //作品评论
        like, //点赞数
        visitors, //浏览数
        intro, //简短介绍

        publishComment:function(comment){ //发布评论
            $.ajax({
                type: "POST",
                url: "/addComment",
                data: { "comment":comment,"uesrNmae":user.name },
                dataType: 'json',
                success: function (myData) {
                   if(myData.data.flag){
                       alert("发布成功");
                   }
                },
                error: function (xhr, type) {
                    console.log(type);
                },
            });
        }, 
        renderComments:function(){//在页面加载评论
            this.comments.forEach(function(item,index,comments){
                var item = document.createElement("div");
                item.className = "item";

                var user = document.createElement("div"); 
                user.className = "user";
                var avatar = document.createElement("div");
                avatar.className = "avatar";
                var uesr_name = document.createElement("div");
                uesr_name.className = "uesr_name";
                
            })
        }, 
        share, //分享作品
    };
}.call(this));