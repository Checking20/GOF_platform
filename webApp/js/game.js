

var rows=10;
var cols=10;
var paintArr=[];
init();

function init() {

    var num=0;
    var game=document.getElementById('game');
    var div;

    var docFrag = document.createDocumentFragment();


    for(var i=0;i<rows*cols;i++){
        div=document.createElement('li');
        div.setAttribute('num',num);
        num++;
        docFrag.appendChild(div);
    }
    game.appendChild(docFrag);
    console.log(docFrag);
}

document.getElementById('game').onclick=function (e) {
    if(e.target.nodeName.toLowerCase()==='li'){
        if(e.target.className==''){
            e.target.className='selected';
        }else {
            e.target.className='';
        }


    }

}
function outPut() {
    var selected=document.querySelectorAll('.selected');
    var numAns=[];
    for(var i=0;i<selected.length;i++){
        numAns.push(selected[i].getAttribute('num'));
    }
    return numAns;
}
var timeId;
document.getElementById('evolve').onclick=function (e) {
    if(e.target.innerText=='演变'){
        timeId=setInterval('evolve()',300);
        document.getElementById('evolve').innerText='暂停';
    }else {
        clearInterval(timeId);
        document.getElementById('evolve').innerText='演变'
    }

}





function evolve() {
    var selected=document.querySelectorAll('li');

    for(var i=0;i<selected.length;i++){
        var num=0;
        var iRow=i%rows;
        var iCol=Math.floor(i/cols);

        for(var a=iCol-1;a<iCol+2;a++){
            for(var b=iRow-1;b<iRow+2;b++){
                if(a==iCol&&b==iRow){
                    continue;
                }
                if(a<0||b<0||a>9||b>9){
                    continue;
                }
                    // console.log(a*cols+b);
                if(selected[a*cols+b].className=='selected'){
                    num++;
                }

            }
        }

        // console.log('block'+' '+i);


        switch (num){
            case 2:
                paintArr[i]=2;
                break;
            case 3:
                paintArr[i]=1;
                break;
            default:
                paintArr[i]=0;
                break;
        }


    }
    paint();
}


function paint() {
    var selected=document.querySelectorAll('li');
    for(var i=0;i<paintArr.length;i++){
        if(paintArr[i]==0){
            selected[i].className='';
        }else if(paintArr[i]==1){
            selected[i].className='selected';
        }
    }
}