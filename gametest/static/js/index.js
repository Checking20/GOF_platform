(function () {
    var loginButton = $(".loginButton");
    var bgDiv = $(".bg");
    var login_register = $(".login_register");
    var login = $(".login");
    var register = $(".register");
    var usernameInput = $(".username");
    var passwordInput = $(".password")
    var username; //用户名
    var password; //密码


    //得到输入框中的用户和密码
    usernameInput.change(function(){
       username =  usernameInput.val();
    })
    passwordInput.change(function(){
       password =  passwordInput.val();
     })

    //点击右上角登录框后弹出模态框和背景
    loginButton.click(function(){
        login_register.css("display","block");        
        bgDiv.css("display","block");
    });

    //登录和注册
    login.click(function(){
        manager.login(username,password);
        if(manager.isLogin){
            login_register.css("display","none");        
            bgDiv.css("display","none");
            loginButton.html(userName);
            common.username = username; //记录用户名
        }
    });
    register.click(function(){
        manager.register(username,password);
        if(manager.register){
            login_register.css("display","none");        
            bgDiv.css("display","none");
            loginButton.html(userName); 
            common.username = username; //记录用户名
        }
    });

    //点击works和begin跳转时
    $(".works").click(function(){
        if(manager.isLogin||manager.isRegister){
            location.href='./share.html';
        }
        else{
            alert("请先登录");
        }
    });
    $(".begin").click(function(){
        if(manager.isLogin||manager.isRegister){
            location.href='./begin.html';
        }
        else{
            alert("请先登录");
        }
    });

    //实际控制登录和注册的manager对象
    var manager = {
        isLogin: false,
        isRegister:true,
        login: function (username, userPass) {
            $.ajax({
                type: "POST",
                url: "/login/",
                data: { "username": username, "password": password },
                dataType: 'json',
                async:false, //同步请求
                success: function (myData) {
                    manager.isLog = myData.data.flag;
                    if (manager.isLog) {
                        alert("登录成功");
                    } else {
                        alert("账号或密码不对")
                    }
                },
                error: function (xhr, type) {
                    console.log(type);
                },
            });
        },
        register: function (username, password) {
            $.ajax({
                type: "POST",
                url: "/register",
                data: { "username": username, "password": password },
                dataType: 'json',
                async:false, //同步请求
                success: function (myData) {
                    if (myData.data.flag) {
                        alert("注册成功");
                    }
                },
                error: function (xhr, type) {
                    console.log(type);
                },
            });
        },
    }
}());
