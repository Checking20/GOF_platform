var prefix='http://106.14.125.177';


document.getElementById('upload').onclick=function () {
    var bool=true;
    for(var i=0;i<paintArr.length;i++){
        if(paintArr[i]!=0){
            bool=false;
            break
        }
    }
    //paintArr = [1,2,3,4,5,6,7,8];
    if(paintArr==[]||bool){
        alert('wrong')
    }else {
        $.ajax({
            //url:prefix+'/AddMap/',
            url:'/AddMap/',
            type:'POST',
            traditional: true,
            data:{"mapContent": paintArr},
            dataType:'JSON',
            success:function (data) {
                console.log(paintArr);
                console.log(1111);
                console.log(data.data.username);
            },
            error:function (data) {
                console.log(data);
            }
        })
    }

    console.log
}

document.getElementById('get').onclick=function () {
    $.ajax({
        //url:prefix+'/getMapDetail/',
        url:'/getMapDetail/',
        type:'POST',
        dataType:'JSON',
        data:{"mapid": 123},
        success:function (data) {
            console.log(data);
        },
        error:function (data) {
            console.log(data);
        }
    })
}