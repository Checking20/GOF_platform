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
            url:prefix+'/AddMap/',
            type:'POST',
            data:JSON.stringify({userId:1,mapContent:paintArr,mapName:'test',mapDescrition:'testDescription'}),
            dataType:'JSON',
            success:function (data) {
                console.log(data);
            },
            error:function (data) {
                console.log(data);
            }
        })
    }

    console.log(JSON.stringify({userId:1,mapContent:paintArr,mapName:'test',mapDescrition:'testDescription'}))
}

document.getElementById('get').onclick=function () {
    $.ajax({
        url:prefix+'/getMapDetail/',
        type:'post',
        dataType:'json',
        data:JSON.stringify({mapId:0}),
        success:function (data) {
            console.log(data);
        },
        error:function (data) {
            console.log(data);
        }
    })
}