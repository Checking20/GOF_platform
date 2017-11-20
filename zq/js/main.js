var workInterfaceMapId = "123";
(function(){

        var manager = {
            isLog:false,
            register:function(userName,userPass){
                $.ajax({
                    type: "POST",
                    url: "/register",
                    data: { "userName": userName,"userPass": userPass},
                    dataType: 'json',
                    success: function (myData) {
                        if(myData.data.flag){
                            alert("注册成功");
                        }
                    },
                    error: function (xhr, type) {
                        console.log(type);
                    },
                });
            },
            login:function(userName,userPass){
                $.ajax({
                    type: "POST",
                    url: "/login",
                    data: { "userName": userName,"userPass": userPass},
                    dataType: 'json',
                    success: function (myData) {
                        manager.isLog = myData.data.flag; 
                        if(manager.isLog){
                            alert("登录成功");
                            user.name=userName;
                            user.avatar = myData.data.avatar;
                        }else{
                            alert("账号或密码不对")
                        }
                    },
                    error: function (xhr, type) {
                        console.log(type);
                    },
                });
            },
            getComments:function(mapId){
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
}());
    