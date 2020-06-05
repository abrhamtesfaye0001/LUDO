

/*

function d(){
    for(var i=0;i<10;i++){
        window.setTimeout(move,i*500,"#gp0","#a"+i);///TODO this shit moves nicely
    }
}

*/


/*

class player {
    constructor(name, color) {
        this.name = name;
        this.color = color;
        this.pieces = this.pieces();

    }

    Piece() {
        var pieceDict = {
            "green": [gp0, gp1, gp2, gp3],
            "red": [rp0, rp1, rp2, rp3],
            "blue": [bp0, bp1, bp2, bp3],
            "yellow": [yp0, yp1, yp2, yp3]
        };

        return pieceDict[this.color];
    }
    toss() {

        return this.getRandomIntInclusive(0, 6);
    }
    getRandomIntInclusive(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }




}
*/

/* ***************************************************************************************************** */
function setParentCell(piece, cell) {
    piece.cell = cell;
}

function enable(piece) {
    piece.active = true;// set active
    hop(piece, piece.path[0]);// hop into the 0th path start
    // piece.cell = piece.path[0];// set the parent cell to the cell that it hopped to
    piece.atStation = false;// set the boolean atStation to false
    addPiece(piece,piece.path[0]);// add the piece to the start's container


}

function disable(piece) {
    piece.active = false;
}

function setActive(tossValue,piece) {
    const once = { once: true };
    // todo fill this one out
    // todo
    // todo
    // todo
    // todo consider the whole game anatomy


}

function nMove(tossValue,piece) {
    // window.clearTimeout(timeOutId);
    var indexOfParentCell = piece.path.indexOf(piece.cell);
    var goalIndex = indexOfParentCell + tossValue + 1;
    var x = indexOfParentCell;
    
    for (var i = indexOfParentCell; i < goalIndex; i++) {
        window.setTimeout(hop, i * 250, piece, piece.path[i]);
        x = i;
        
    }
    // eval(`window.clearTimeout(timeOutId${i-1});`);
    
    // piece.cell = piece.path[x];//todo just commented
    // piece.path[x].addPiece(piece);    //todo append the piece to the cell object
    // addPiece(piece, piece.path[x]);
    window.setTimeout(addPiece,(x+0.5)*250,piece,piece.path[x]);
    console.log(piece.path[x]);
}


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

}

function reset(piece) {
    hop(piece, piece.station);
    // removePiece(piece,piece.cell);
    addPiece(piece,piece.station);
}

function Color(piece) {
    var dict = { "b": "blue", "g": "green", "r": "red", "y": "yellow" };
    piece.color = dict[piece.id[1]];
    return dict[piece.id[1]];
}

function Path(piece) {
    var paths = { "blue": bluePath, "green": greenPath, "red": redPath, "yellow": yellowPath };
    piece.path = paths[Color(piece)];
    return piece.path;
}

function addPiece(piece,cell) {
    removePiece(piece,piece.cell);
    // console.log(cell.container.indexOf(piece));

    if (isSafe(piece,cell)) {
        // cell.container.push(piece);
        cell.container.push(piece);
        piece.cell = cell;
        // TODO 
        // console.log(`added ${piece.id} to ${cell.id}`);

    }
    else {
        console.log("not safe");
        // for (var i = 0; i < cell.container.length; i++) {
        //     console.log(cell.container[i].id);
        //     // if (cell.container[i].color != piece.color) {
        //         reset(cell.container[i]);//TODO resets the other piece to it's original station
        //         cell.container.splice(i, 1);// removes the different piece from the cell
        //         // after finishing off other pieces we append the piece to the cell   
        //     // }
        // }
        var enemies = cell.container;
        
        var x = cell.container.length;
        for(var y=0;y<x;y++){
            reset(cell.container[x-y-1]);
        }
        cell.container.push(piece);
        piece.cell = cell;
}
    
}



function removePiece(piece,cell){
    cell.container.splice(cell.container.indexOf(piece),1);
}

function remove(value,arr){
    for (var i=0;i<arr.length;i++){
        if (arr[i]==value){
            arr.splice(i,1);
        }
    }
}



function isSafe(piece,cell) {
    if (cell.type == "start" || cell.type == "homeRun"|| cell.type == "home" ||cell.container.length == 0 ) {
        // console.log("true safe");
        return true;
    }
    else {
        // console.log("not safe");
        for (var i = 0; i < cell.container.length; i++) {
            if (cell.container[i].color != piece.color) {
                // console.log("bad color found");
                return false;
            }

        }
        return true;
    }
}

//#######################################################################################################################

class Piece {
    constructor(id, station) {
        this.id = id;
        this.station = station;
        this.active = false;
        this.atStation = true;
        this.color = null;
        this.path = null;
        this.cell = station;
    }
    DOM() {
        return document.querySelector(this.id);
    }

}

class Cell {
    constructor(id, type) {
        this.type = type;
        this.id = id;
        this.container = [];
    }

}


class player{
    constructor(color){
        this.color = color;
    }
}

a0 = new Cell("#a0", "open");
a1 = new Cell("#a1", "open");
a2 = new Cell("#a2", "open");
a3 = new Cell("#a3", "open");
a4 = new Cell("#a4", "open");
a5 = new Cell("#a5", "open");
a6 = new Cell("#a6", "open");
a7 = new Cell("#a7", "open");
a8 = new Cell("#a8", "open");
a9 = new Cell("#a9", "open");
a10 = new Cell("#a10", "open");
a11 = new Cell("#a11", "open");
a12 = new Cell("#a12", "open");
a13 = new Cell("#a13", "open");
a14 = new Cell("#a14", "open");
a15 = new Cell("#a15", "open");
a16 = new Cell("#a16", "open");
a17 = new Cell("#a17", "open");
a18 = new Cell("#a18", "open");
a19 = new Cell("#a19", "open");
a20 = new Cell("#a20", "open");
a21 = new Cell("#a21", "open");
a22 = new Cell("#a22", "open");
a23 = new Cell("#a23", "open");
a24 = new Cell("#a24", "open");
a25 = new Cell("#a25", "open");
a26 = new Cell("#a26", "open");
a27 = new Cell("#a27", "open");
a28 = new Cell("#a28", "open");
a29 = new Cell("#a29", "open");
a30 = new Cell("#a30", "open");
a31 = new Cell("#a31", "open");
a32 = new Cell("#a32", "open");
a33 = new Cell("#a33", "open");
a34 = new Cell("#a34", "open");
a35 = new Cell("#a35", "open");
a36 = new Cell("#a36", "open");
a37 = new Cell("#a37", "open");
a38 = new Cell("#a38", "open");
a39 = new Cell("#a39", "open");
a40 = new Cell("#a40", "open");
a41 = new Cell("#a41", "open");
a42 = new Cell("#a42", "open");
a43 = new Cell("#a43", "open");
a44 = new Cell("#a44", "open");
a45 = new Cell("#a45", "open");
a46 = new Cell("#a46", "open");
a47 = new Cell("#a47", "open");

r0 = new Cell("#r0", "start");
r1 = new Cell("#r1", "homeRun");
r2 = new Cell("#r2", "homeRun");
r3 = new Cell("#r3", "homeRun");
r4 = new Cell("#r4", "homeRun");
r5 = new Cell("#r5", "homeRun");
r6 = new Cell("#r6", "home");

r7 = new Cell("#r7", "station");
r8 = new Cell("#r8", "station");
r9 = new Cell("#r9", "station");
r10 = new Cell("#r10", "station");

g0 = new Cell("#g0", "start");
g1 = new Cell("#g1", "homeRun");
g2 = new Cell("#g2", "homeRun");
g3 = new Cell("#g3", "homeRun");
g4 = new Cell("#g4", "homeRun");
g5 = new Cell("#g5", "homeRun");
g6 = new Cell("#g6", "home");

g7 = new Cell("#g7", "station");

g8 = new Cell("#g8", "station");
g9 = new Cell("#g9", "station");
g10 = new Cell("#g10", "station");

b0 = new Cell("#b0", "start");
b1 = new Cell("#b1", "homeRun");
b2 = new Cell("#b2", "homeRun");
b3 = new Cell("#b3", "homeRun");
b4 = new Cell("#b4", "homeRun");
b5 = new Cell("#b5", "homeRun");
b6 = new Cell("#b6", "home");
b7 = new Cell("#b7", "station");
b8 = new Cell("#b8", "station");
b9 = new Cell("#b9", "station");
b10 = new Cell("#b10", "station");

y0 = new Cell("#y0", "start");
y1 = new Cell("#y1", "homeRun");
y2 = new Cell("#y2", "homeRun");
y3 = new Cell("#y3", "homeRun");
y4 = new Cell("#y4", "homeRun");
y5 = new Cell("#y5", "homeRun");
y6 = new Cell("#y6", "home");
y7 = new Cell("#y7", "station");
y8 = new Cell("#y8", "station");
y9 = new Cell("#y9", "station");
y10 = new Cell("#y10", "station");


redPath = [r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, r1, r2, r3, r4, r5, r6];
greenPath = [g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, g1, g2, g3, g4, g5, g6];
bluePath = [b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6];
yellowPath = [y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, y1, y2, y3, y4, y5, y6];





rp0 = new Piece("#rp0", r7, redPath);
rp1 = new Piece("#rp1", r8, redPath);
rp2 = new Piece("#rp2", r9, redPath);
rp3 = new Piece("#rp3", r10, redPath);





gp0 = new Piece("#gp0", g7, greenPath);
gp1 = new Piece("#gp1", g8, greenPath);
gp2 = new Piece("#gp2", g9, greenPath);
gp3 = new Piece("#gp3", g10, greenPath);



bp0 = new Piece("#bp0", b7, bluePath);
bp1 = new Piece("#bp1", b8, bluePath);
bp2 = new Piece("#bp2", b9, bluePath);
bp3 = new Piece("#bp3", b10, bluePath);


yp0 = new Piece("#yp0", y7, yellowPath);
yp1 = new Piece("#yp1", y8, yellowPath);
yp2 = new Piece("#yp2", y9, yellowPath);
yp3 = new Piece("#yp3", y10, yellowPath);

// addPiece(gp0,g7);


function placeAtStation() {
    hop(gp0, g7);

    hop(gp1, g8);
    hop(gp2, g9);
    hop(gp3, g10);

    hop(yp0, y7);
    hop(yp1, y8);
    hop(yp2, y9);
    hop(yp3, y10);

    hop(rp0, r7);
    hop(rp1, r8);
    hop(rp2, r9);
    hop(rp3, r10);

    hop(bp0, b7);
    hop(bp1, b8);
    hop(bp2, b9);
    hop(bp3, b10);



}

function pathAssign() {
    pieces = [rp0, rp1, rp2, rp3, gp0, gp1, gp2, gp3, yp0, yp1, yp2, yp3, bp0, bp1, bp2, bp3];
    pieces.forEach(i => {
        i.color = Color(i);
        addPiece(i,i.station);//initial place at the stations
        Path(i);
    });
}


///window.onload(window.setTimeout(alertMe,10000));
try {
    window.onresize(placeAtStation);    
} catch (TypeError) {
    
}

try {

    window.onload(window.setTimeout(placeAtStation, 10));
} catch (TypeError) {
    try {
        window.onload(window.setTimeout(pathAssign, 10));
    } catch (TypeError) {

    }

}




/* ***************************************************************************************************** */







































