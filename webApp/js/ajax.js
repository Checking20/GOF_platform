document.getElementById('upload').onclick=function () {
    var bool=true;
    for(var i=0;i<paintArr.length;i++){
        if(paintArr[i]!=0){
            bool=false;
            break
        }
    }
    if(paintArr==[]||bool){
        alert('wrong')
    }else {
        $.ajax({
            url:'/upLoad',
            type:'POST',
            data:paintArr,
            dataType:'JSON',
            success:function (data) {
                console.log(data);
            },
            error:function (data) {
                console.log(data);
            }
        })
    }


}

document.getElementById('get').onclick=function () {
    $.ajax({
        url:'/getImg',
        type:'get',
        dataType:'json',
        success:function (data) {
            console.log(data);
        },
        error:function (data) {
            console.log(data);
        }
    })
}