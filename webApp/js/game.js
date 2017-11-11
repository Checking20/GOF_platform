init();


function init() {
    var rows=10;
    var cols=10;
    var num=0;
    var game=document.getElementById('game');
    var div;

    var docFrag = document.createDocumentFragment();


    for(var i=0;i<rows;i++){
        for (var j=0;j<cols;j++){
            div=document.createElement('li');
            div.setAttribute('num',num);
            num++;
            docFrag.appendChild(div);
        }
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

function evolve() {
    
}
