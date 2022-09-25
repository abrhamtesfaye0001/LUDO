import {Cell,Piece,Player} from "./classes.js";
import {redPath,greenPath,bluePath,yellowPath} from "./objects.js";


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
