window.onload = function () {
    var works = $(".works");
    var contents = [1,2,3,4,5,6,7];
    function getWorks(type) {
        $.ajax({
            type: "GET",
            url: "/getWorks",
            data: { "type": type },
            dataType: 'json',
            success: function (myData) {
                
            },
            error: function (xhr, type) {
                console.log(type);
            },
        });
    }

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