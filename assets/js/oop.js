
class piece{
    constructor(id,station,path){
        this.id = id;
        this.station  = station;
        this.active = false;
        this.atStation = true;
        this.color = this.Color();
        // this.path = this.Path;
        this.cell = station;

        this.path = greenPath;
        // console.log(greenPath);
        // this.path = ()=>{return this.Path()};
        // console.log(this.path);

        this.binary = 0;// control 0 or 1

        // this.paths = {"blue":bluePath,"green":greenPath,"red":redPath,"yellow":yellowPath};
        // this.path = this.paths[this.color];
        // console.log(this.id);
    }

    setParentCell(id){
        this.cell = id;
    }
    DOM(){
        return document.querySelector(this.id);
    }
    

    enable(){//able to move using tossvalue
        this.active = true;
        var paths = {"blue":bluePath,"green":greenPath,"red":redPath,"yellow":yellowPath};
        var x = greenPath;
        
        piece.hop(this,greenPath[0]);
        this.cell = greenPath[0];
        this.atStation = false;
        console.log("enable");
        

    }

    disable(){// unable to move
        this.active = false;
    }

    
    setActive(tossValue){
            const once = {once:true};
            
            if (tossValue == 6 && this.station == this.cell && this.atStation==true){
                this.DOM().addEventListener("click",this.enable,once); 
                this.DOM().classList.add("zoomer");
                // this.enable();
            }
            else{
            var indexOfParentCell = this.path.indexOf(this.cell);
            
                
            if (indexOfParentCell+tossValue < this.path.length){//todo some attention to math
                this.DOM().addEventListener("click",this.nMove(tossValue),once);
                
            }
            // this.DOM().classList.add("zoomer");
            // this.binary = 1;

            }


       
        
        
        

        
    }
    setInactive(){
        this.DOM().classList.remove("zoomer");
        this.binary = 0;
    }

    reset(){
        this.hop(this,this.station);
        this.cell = this.station;
    }
    Color(){
        var dict = {"b":"blue","g":"green","r":"red","y":"yellow"};
        return dict[this.id[1]];
    }

    Path(){
        var paths = {"blue":bluePath,"green":greenPath,"red":redPath,"yellow":yellowPath};
        this.path =  paths[this.color];
    }
    nMove(tossValue){
        // this.path
        // this.cell
        var indexOfParentCell = this.path.indexOf(this.cell);
        var goalIndex = indexOfParentCell+tossValue+1;
        var x=indexOfParentCell;
        for(var i=indexOfParentCell;i<=goalIndex;i++){
            window.setTimeout(this.hop,i*500,this,this.path[i]);
            x=i;
        }
        this.setParentCell(this.path[x]);
        //todo append the piece to the cell object


        }
    // hop(piece,destinationCell){
    static hop(piece,destinationCell){
        try {
            
        var currPiece = document.querySelector(piece.id);
        var dest = document.querySelector(destinationCell.id);
        
        destTop = dest.getBoundingClientRect().top;
        destLeft = dest.getBoundingClientRect().left;
    
        destWidth = dest.getBoundingClientRect().width;
    
        pieceWIdth = currPiece.getBoundingClientRect().width;
    
        y = destTop + (destWidth-pieceWIdth)/2;
        x = destLeft + (destWidth-pieceWIdth)/2;
            switch(eval(piece.id[3])){
                case 0:
                    y=y+2+"px";
                    x=x+0+"px";
                    break;
                case 1:
                    y=y+2+"px";
                    x=x+2+"px";
                    break;
                case 2:
                    y=y+0+"px";
                    x=x+0+"px";
                    break;
                case 3:
                    y=y+0+"px";
                    x=x+2+"px";
                    break;
            }
        currPiece.style.top = y;
        currPiece.style.left = x;
        } catch (TypeError) {

            
        }
        
    }

}

class cell {
    constructor(id, type) {//start,open,gate,homeRun,home
        this.type = type;
        this.id = id;
        this.container = []
        

    }
    element(){
        return document.querySelector(this.id);
    }
    addPiece(piece) {
        if (this.type != "start" && this.isSafe(piece)) {
            this.container.push(piece);
            // TODO insert html part of moving
            
        }
        else {
            for (var i = 0; i < this.container.length; i++) {
                if (this.container[i].color != piece.color) {
                    this.container[i].reset();//TODO resets the piece to it's original station
                    this.container.splice(i, 1);// removes the different piece from the 
                }
            }
        }

    }
    isSafe(piece) {
        if (this.container.length == 0) {
            return true;
        }
        else {
            for (var i = 0; i < this.container.length; i++) {
                if (this.container[i].color != piece.color) {
                    return false;
                }

            }
            return true;
        }
    }


}


a0 = new cell("#a0", "open");
a1 = new cell("#a1", "open");
a2 = new cell("#a2", "open");
a3 = new cell("#a3", "open");
a4 = new cell("#a4", "open");
a5 = new cell("#a5", "open");
a6 = new cell("#a6", "open");
a7 = new cell("#a7", "open");
a8 = new cell("#a8", "open");
a9 = new cell("#a9", "open");
a10 = new cell("#a10", "open");
a11 = new cell("#a11", "open");
a12 = new cell("#a12", "open");
a13 = new cell("#a13", "open");
a14 = new cell("#a14", "open");
a15 = new cell("#a15", "open");
a16 = new cell("#a16", "open");
a17 = new cell("#a17", "open");
a18 = new cell("#a18", "open");
a19 = new cell("#a19", "open");
a20 = new cell("#a20", "open");
a21 = new cell("#a21", "open");
a22 = new cell("#a22", "open");
a23 = new cell("#a23", "open");
a24 = new cell("#a24", "open");
a25 = new cell("#a25", "open");
a26 = new cell("#a26", "open");
a27 = new cell("#a27", "open");
a28 = new cell("#a28", "open");
a29 = new cell("#a29", "open");
a30 = new cell("#a30", "open");
a31 = new cell("#a31", "open");
a32 = new cell("#a32", "open");
a33 = new cell("#a33", "open");
a34 = new cell("#a34", "open");
a35 = new cell("#a35", "open");
a36 = new cell("#a36", "open");
a37 = new cell("#a37", "open");
a38 = new cell("#a38", "open");
a39 = new cell("#a39", "open");
a40 = new cell("#a40", "open");
a41 = new cell("#a41", "open");
a42 = new cell("#a42", "open");
a43 = new cell("#a43", "open");
a44 = new cell("#a44", "open");
a45 = new cell("#a45", "open");
a46 = new cell("#a46", "open");
a47 = new cell("#a47", "open");

r0 = new cell("#r0", "start");
r1 = new cell("#r1", "homeRun");
r2 = new cell("#r2", "homeRun");
r3 = new cell("#r3", "homeRun");
r4 = new cell("#r4", "homeRun");
r5 = new cell("#r5", "homeRun");
r6 = new cell("#r6", "home");
r7 = new cell("#r7", "station");
r8 = new cell("#r8", "station");
r9 = new cell("#r9", "station");
r10 = new cell("#r10", "station");

g0 = new cell("#g0", "start");
g1 = new cell("#g1", "homeRun");
g2 = new cell("#g2", "homeRun");
g3 = new cell("#g3", "homeRun");
g4 = new cell("#g4", "homeRun");
g5 = new cell("#g5", "homeRun");
g6 = new cell("#g6", "home");
g7 = new cell("#g7", "station");
g8 = new cell("#g8", "station");
g9 = new cell("#g9", "station");
g10 = new cell("#g10", "station");

b0 = new cell("#b0", "start");
b1 = new cell("#b1", "homeRun");
b2 = new cell("#b2", "homeRun");
b3 = new cell("#b3", "homeRun");
b4 = new cell("#b4", "homeRun");
b5 = new cell("#b5", "homeRun");
b6 = new cell("#b6", "home");
b7 = new cell("#b7", "station");
b8 = new cell("#b8", "station");
b9 = new cell("#b9", "station");
b10 = new cell("#b10", "station");

y0 = new cell("#y0", "start");
y1 = new cell("#y1", "homeRun");
y2 = new cell("#y2", "homeRun");
y3 = new cell("#y3", "homeRun");
y4 = new cell("#y4", "homeRun");
y5 = new cell("#y5", "homeRun");
y6 = new cell("#y6", "home");
y7 = new cell("#y7", "station");
y8 = new cell("#y8", "station");
y9 = new cell("#y9", "station");
y10 = new cell("#y10", "station");


redPath = [r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,b0, a12, a13, a14, a15, a16, a17, a18 ,a19, a20, a21, a22, a23,y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35,g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46,r1,r2,r3,r4,r5,r6];
greenPath = [g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47,r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11,b0, a12, a13, a14, a15, a16, a17, a18 , a19, a20, a21, a22, a23,y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, g1, g2,g3,g4,g5,g6];
bluePath = [b0, a12, a13, a14, a15, a16, a17, a18 , a19, a20, a21, a22, a23,y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35,g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47,r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10,b1,b2,b3,b4,b5,b6];
yellowPath = [y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18 , a19, a20, a21, a22,y1,y2,y3,y4,y5,y6];





rp0 =new piece("#rp0",r7,redPath);
rp1 =new piece("#rp1",r8,redPath);
rp2 =new piece("#rp2",r9,redPath);
rp3 =new piece("#rp3",r10,redPath);





gp0 =new piece("#gp0",g7,greenPath);
gp1 =new piece("#gp1",g8,greenPath);
gp2 =new piece("#gp2",g9,greenPath);
gp3 =new piece("#gp3",g10,greenPath);



bp0 =new piece("#bp0",b7,bluePath);
bp1 =new piece("#bp1",b8,bluePath);
bp2 =new piece("#bp2",b9,bluePath);
bp3 =new piece("#bp3",b10,bluePath);


yp0 =new piece("#yp0",y7,yellowPath);
yp1 =new piece("#yp1",y8,yellowPath);
yp2 =new piece("#yp2",y9,yellowPath);
yp3 =new piece("#yp3",y10,yellowPath);


class board {//TODO each type of piece needs its own cells array
    constructor() {


    }

}


class station {
    constructor(color) {//green,yellow,red,blue
        this.color = color;
        this.cells = [];

    }
    add(cell) {
        this.cells.push(cell);
    }
    remove(cell) {
        this.cells.remove(cell);
    }

}








// document.querySelector("#gp0").addEventListener("click",myOption);










// function resize() {
//     center = document.querySelector("#center");
//     anchor = document.querySelector("#anchor");
//     center.style.top = anchor.getBoundingClientRect().top + "px";
//     center.style.left = anchor.getBoundingClientRect().left + "px";
//     center.style.width = anchor.getBoundingClientRect().width * 3 + 1 + "px";
// }
// resize()// resize the center to screen size












// function move(pieceId, destinationId) {
//     piece = document.querySelector(pieceId);
//     origin = document.querySelector("#" + piece.parentNode.id);
//     destination = document.querySelector(destinationId);
//     // translate it to new position by the width of the cells
//     oTop = origin.getBoundingClientRect().top;
//     oLeft = origin.getBoundingClientRect().left;
//     oWidth = origin.getBoundingClientRect().width;


//     dTop = destination.getBoundingClientRect().top;
//     dLeft = destination.getBoundingClientRect().left;
//     dWidth = destination.getBoundingClientRect().width;


//     // piece.style.transition = "2s"

//     myTop = Math.sign(dTop - oTop) * oWidth + "px";
//     myLeft = Math.sign(dLeft - oLeft) * oWidth + "px";

//     piece.style.transform = "translate(" + myLeft + "," + myTop + ")";
//     // piece.style.transition = "1s";
//     destination.appendChild(piece);

//     piece.style.transform = "translate(0px,-21px)";
//     piece.style.transform = "translate(0px,0px)";

//     var x=-22*( piece.parentNode.children.length-1) + "px";
//     piece.style.transform = "translate(0px,"+x+")";

//     piece.style.top = "0px";

    



// }

function hop(piece, destinationCell) {
    try {

        var currPiece = document.querySelector(piece.id);
        var dest = document.querySelector(destinationCell.id);

        destTop = dest.getBoundingClientRect().top;
        destLeft = dest.getBoundingClientRect().left;

        destWidth = dest.getBoundingClientRect().width;

        pieceWIdth = currPiece.getBoundingClientRect().width;

        y = destTop + (destWidth - pieceWIdth) / 2;
        x = destLeft + (destWidth - pieceWIdth) / 2;
        // console.log("reached gggggggggg");
        switch (eval(piece.id[3])) {
            case 0:
                y = y + 2 + "px";
                x = x + 0 + "px";
                break;
            case 1:
                y = y + 2 + "px";
                x = x + 2 + "px";
                break;
            case 2:
                y = y + 0 + "px";
                x = x + 0 + "px";
                break;
            case 3:
                y = y + 0 + "px";
                x = x + 2 + "px";
                break;
        }
        currPiece.style.top = y;
        currPiece.style.left = x;
    } catch (TypeError) {


    }
    // console.log("reached heare");

}


function placeAtStation(){
    hop(gp0,g7);
    
    hop(gp1,g8);
    hop(gp2,g9);
    hop(gp3,g10);

    hop(yp0,y7);
    hop(yp1,y8);
    hop(yp2,y9);
    hop(yp3,y10);

    hop(rp0,r7);
    hop(rp1,r8);
    hop(rp2,r9);
    hop(rp3,r10);

    hop(bp0,b7);
    hop(bp1,b8);
    hop(bp2,b9);
    hop(bp3,b10);
    
    
    
}


///window.onload(window.setTimeout(alertMe,10000));
try {
    window.onload(window.setTimeout(placeAtStation,10));
} catch (TypeError) {
    
}



// window.addEventListener("load",function(){resize()});
// document.addEventListener("resize",function(){resize();})
// window.onresize = function(){resize();}
/*

function d(){
    for(var i=0;i<10;i++){
        window.setTimeout(move,i*500,"#gp0","#a"+i);///TODO this shit moves nicely
    }
}

*/


// function enable(piece){//able to move using tossvalue
//     piece.active = true;
//     var paths = {"blue":bluePath,"green":greenPath,"red":redPath,"yellow":yellowPath};
//     var x = greenPath;
//     hop(piece,x);
//     piece.cell = piece.path[0];
//     piece.atStation = false;

// }