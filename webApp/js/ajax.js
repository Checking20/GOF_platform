var prefix='http://106.14.125.177';

document.getElementById('configUpload').onclick=function () {
    var name=document.getElementById('inputName').value;
    var description=document.getElementById('inputDescription').value;
    if(name==''||description==''){
        alert('input error');
    }else{
        $.ajax({
            url:prefix+'/AddState/',
            type:'POST',
            traditional:true,
            // data:JSON.stringify({userId:1,mapContent:paintArr,mapName:'test',mapDescrition:'testDescription'}),
            data:{content:paintArr,statename:name,description:description},
            dataType:'JSON',
            success:function (data) {
                console.log(data);
                $('#myModal').modal('hide');
                alert('success');
            },
            error:function (data) {
                console.log(data);
                $('#myModal').modal('hide');
                alert('failure');
            }
        })
    }

}


document.getElementById('upload').onclick=function () {
    var bool=true;
    for(var i=0;i<paintArr.length;i++){
        if(paintArr[i]!=0){
            bool=false;
            break
        }
    }
    if(bool){
        alert('wrong')
    }else {
        $('#myModal').modal('show');

    }
}

document.getElementById('get').onclick=function () {
    $.ajax({
        url:prefix+'/getMapDetail/',
        type:'POST',
        dataType:'json',
        data:JSON.stringify({mapId:12341234}),
        success:function (data) {
            console.log(data);
        },
        error:function (data) {
            console.log(data);
        }
    })

    console.log({mapId:12341234});
   
}