var prefix='http://106.14.125.177';


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
            //url:prefix+'/AddMap/',
            url:'/AddMap/',
            type:'POST',
            data:{userId:1,mapContent:paintArr,mapName:'test',mapDescrition:'testDescription'},
            dataType:'JSON',
            success:function (data) {
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
        type:'post',
        dataType:'json',
        data:{mapId:1},
        success:function (data) {
            console.log(data);
        },
        error:function (data) {
            console.log(data);
        }
    })
}