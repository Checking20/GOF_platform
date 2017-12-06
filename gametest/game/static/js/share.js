window.onload = function () {
    var works = $(".works");
    var prefix = 'http://106.14.125.177';
    var contents = ['mywork', 'perfectGraph', 'wow', 'hey look at me', 'please clike me', 'yeah', 'zzzz'];

    //得到某一栏目下的所有作品
    function getWorks(type) {
        works.empty();//删除上次加载的works
        $.ajax({
            type: "POST",
            url: prefix + "/getWorks/",
            data: { "type": type },
            dataType: 'json',
            success: function (myData) {
                myData.data.forEach(function (item, index, arr) {
                    addWork(item);
                })
            },
            error: function (xhr, type) {
                console.log(type);
            },
        });
    }


    //添加一个作品
    function addWork(content) {
        var work = document.createElement("div");
        work.className = "work"+" " + content.stateid;
        work.innerHTML = content;
        works.append(work);
    }

    //初始化界面
    function init() {
        getWorks("hot");
    }
    // init();
    //测试代码
    contents.forEach(function (item, index, arr) {
        addWork(item);
    })

    //切换作品所属栏目并加载其下作品
    // $(".sort_nav").click(function (event) {
    //     var myTarget = $(event.target);
    //     var type = myTarget.attr("class").split(" ")[0];
    //     if (type != "sort_nav") {
    //         myTarget.siblings().css("backgroundColor", "#e1ebf4");
    //         myTarget.css("backgroundColor", "#575455");
    //         getWorks(type);
    //     }
    // });

    //点击某个作品跳转到该作品详细界面
    works.click(function(e){
        var myTarget = $(e.target);
        var mapId = myTarget.attr("class").split(" ")[1];
        if(myTarget.attr("class").split(" ")[0]=="work"){
            window.location.href='./work.html';
            common.workInterfaceMapId = mapId; //记录mapId
        }
    })
}