window.onload = function () {
    var works = $(".works");
    var contents = [1,2,3,4,5,6,7];
    function getWorks(type) {
        works.empty();//删除上次加载works
        $.ajax({
            type: "GET",
            url: "/getWorks",
            data: { "type": type },
            dataType: 'json',
            success: function (myData) {
                myData.data.forEach(function(item,index,arr){
                    addWork(item);
                })
            },
            error: function (xhr, type) {
                console.log(type);
            },
        });
    }
    

    //添加一个作品
    function addWork(content){
        var work = document.createElement("div");
        work.className = "work";
        work.innerHTML = content;

        works.append(work);
    }

    //初始化界面
    function init(){
        getWorks("hot");
    }
    //测试代码
    contents.forEach(function(item,index,arr){
        addWork(item);
    })
   
    //切换作品所属栏目
    $(".sort_nav").click(function (event) {
        var myTarget = $(event.target);
        var type = myTarget.attr("class").split(" ")[0];
        if(type!="sort_nav"){
            myTarget.siblings().css("backgroundColor","#e1ebf4");
            myTarget.css("backgroundColor","#575455");
            getWorks(type);
        }
      });
}