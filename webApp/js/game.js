

var rows=20;
var cols=20;
var paintArr=[];
for(var i=0;i<rows*cols;i++){
    paintArr[i]=0;
}
var colorState=1;
init();
var state=0;
function init() {
    document.getElementById('text').innerText='速度: '+document.getElementById('range').value+'ms';
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

    if(e.target.nodeName.toLowerCase()==='li'&&e.target.getAttribute('num')!=undefined){
        if(e.target.className==''){
            switch (colorState){
                case 1:
                    e.target.className='active lightblue';
                    break;
                case 2:
                    e.target.className='active purple';
                    break;
                case 3:
                    e.target.className='active red';
                    break;
                case 4:
                    e.target.className='active yellow';
                    break;
            }

            paintArr[e.target.getAttribute('num')]=1;
        }else {
            e.target.className='';
            paintArr[e.target.getAttribute('num')]=0;
        }
    }
}



function outPut() {
    var selected=document.querySelectorAll('.active');
    var numAns=[];
    for(var i=0;i<selected.length;i++){
        numAns.push(selected[i].getAttribute('num'));
    }
    return numAns;
}

var timeId;

document.getElementById('evolve').onclick=function (e) {
    if(e.target.innerText=='演变'){
        timeId=setInterval('evolve()',document.getElementById('range').value);
        document.getElementById('evolve').innerText='暂停';
        state=1;
    }else {
        clearInterval(timeId);
        document.getElementById('evolve').innerText='演变';
        state=0;
    }

}
document.getElementById('range').oninput=function () {
    document.getElementById('text').innerText='速度: '+document.getElementById('range').value+'ms';
    if(state==0){

    }else {
        clearInterval(timeId);
        timeId=setInterval('evolve()',document.getElementById('range').value);
    }

}




function evolve() {

    var selected=document.querySelectorAll('#game>li');

    for(var i=0;i<selected.length;i++){
        var num=0;
        var iRow=i%rows;
        var iCol=Math.floor(i/cols);

        for(var a=iCol-1;a<iCol+2;a++){
            for(var b=iRow-1;b<iRow+2;b++){
                if(a==iCol&&b==iRow){
                    continue;
                }
                if(a<0||b<0||a>cols-1||b>rows-1){
                    continue;
                }

                if(selected[a*cols+b].className=='active lightblue'||selected[a*cols+b].className=='active purple'||selected[a*cols+b].className=='active red'||selected[a*cols+b].className=='active yellow'){
                    num++;
                }

            }
        }

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
    paint(paintArr);
}

function paint(arr) {
    var selected=document.querySelectorAll('#game>li');
    for(var i=0;i<arr.length;i++){
        if(arr[i]==0){
            selected[i].className='';
        }else if(arr[i]==1){
            switch (colorState){
                case 1:
                    selected[i].className='active lightblue';
                    break;
                case 2:
                    selected[i].className='active purple';
                    break;
                case 3:
                    selected[i].className='active red';
                    break;
                case 4:
                    selected[i].className='active yellow';
                    break;
            }

        }
    }
}



document.getElementById('leftLine').onclick=function (e) {
    if(e.target.nodeName.toLowerCase()=='li'){
        var active=document.querySelectorAll('.active');

        switch (e.target.className){
            case 'lightblue':
                for(var a=0;a<active.length;a++){
                    active[a].className='active lightblue';
                }
                colorState=1;
                break;
            case 'purple':

                for(var b=0;b<active.length;b++){
                    active[b].className='active purple';
                }
                colorState=2;
                break;
            case 'red':

                for(var c=0;c<active.length;c++){
                    active[c].className='active red';
                }
                colorState=3;
                break;
            case 'yellow':

                for(var d=0;d<active.length;d++){
                    active[d].className='active yellow';
                }
                colorState=4;
                break;
        }
    }
}