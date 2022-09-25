class Piece {
    constructor(id, station) {
        this.id = id;
        this.station = station;
        this.cell = station;

        this.active = false;
        this.atStation = true;

        this.color = this.getColor();
        this.path = this.getPath();// array of cells
        window.setTimeout(() => { this.dom = this.getDom(); }, 1);
        window.addEventListener("resize", () => { this.reAllocate(); });
        window.addEventListener("load", () => { this.reAllocate(); });


        // var domPromise = new Promise((resolve,reject)=>{
        //     resolve(this.dom = this.getDom());
        // });

        // domPromise.then(response=>{
        //     window.addEventListener("resize", () => { this.reAllocate(); });
        //     window.addEventListener("load", () => { this.reAllocate(); });
        // })





    }


    getColor() {
        var colorMap = {
            "g": "green",
            "y": "yellow",
            "r": "red",
            "b": "blue"
        };

        return colorMap[this.id[1]];
    }
    getPath() {
        var pathMap = {
            "red": [r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, r1, r2, r3, r4, r5, r6],
            "green": [g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, g1, g2, g3, g4, g5, g6],
            "blue": [b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6],
            "yellow": [y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, y1, y2, y3, y4, y5, y6]
        }
        return pathMap[this.color];
    }
    getDom() {
        return document.querySelector(this.id);
    }
    hop(destinationCell) {
        // try {
        console.log(this.id, this.cell.id);
        var currPiece = this.dom;
        var dest = destinationCell.dom;

        var destTop = dest.getBoundingClientRect().top;
        var destLeft = dest.getBoundingClientRect().left;

        var destWidth = dest.getBoundingClientRect().width;

        var pieceWIdth = currPiece.getBoundingClientRect().width;

        var y = destTop + (destWidth - pieceWIdth) / 2;
        var x = destLeft + (destWidth - pieceWIdth) / 2;
        switch (eval(this.id[3])) {// offsets
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
        // } catch (TypeError) {
        //     console.log("error");
        // }
    }
    nMove(tossValue) {

        var indexOfParentCell = this.path.indexOf(this.cell);
        var goalIndex = indexOfParentCell + tossValue + 1;
        if (this.cell == this.station) {

        }
        else {

            var i = indexOfParentCell;
            const sleep = milliseconds => {
                return new Promise(resolve => setTimeout(resolve, milliseconds));

            };

            var piece = this;
            function move(i) {
                if (i == goalIndex) {
                    piece.path[i - 1].addPiece(piece);
                }
                else {
                    sleep(250).then(() => {
                        move(i + 1);
                        piece.hop(piece.path[i]);
                    })
                }
            }
            move(i);
        }

    }

    enable() {

        this.active = true;
        this.hop(this.path[0]);
        this.atStation = false;
        this.path[0].addPiece(this);
    }

    reset() {
        this.hop(this.station);
        this.station.addPiece(this);
    }

    // placeAtStation() {
    //     this.reset();// todo have some suspision
    // }

    reAllocate() {
        var cell = document.querySelector(this.cell.id);
        var piece = document.querySelector(this.id);

        window.setTimeout(() => {
            var cellTop = cell.getBoundingClientRect().top;
            var cellLeft = cell.getBoundingClientRect().left;
            var cellWidth = cell.getBoundingClientRect().width;
            var pieceWidth = piece.getBoundingClientRect().width;
            piece.style.left = 1 + cellLeft + (cellWidth - pieceWidth) / 2 + "px";
            piece.style.top = 1 + cellTop + (cellWidth - pieceWidth) / 2 + "px";
        }, 100)


    }

}



// gp0 = new Piece("#gp0","#g7");
class Cell {
    constructor(id, type) {
        this.type = type;
        this.id = id;
        this.container = [];
        window.setTimeout(() => { this.dom = this.getDom(); }, 25);
    }
    getDom() {
        return document.querySelector(this.id);
    }
    addPiece(piece) {
        piece.cell.removePiece(piece);
        if (this.isSafeFor(piece)) {
            this.container.push(piece);
            piece.cell = this;

        }
        else {
            console.log("not safe");
            var enemies = this.container;

            var x = enemies.length;

            for (var y = 0; y < x; y++) {
                this.container[x - y - 1].reset();////////////////////////// todo edit her
            }
            this.container.push(piece);
            piece.cell = this;
        }


    }
    removePiece(piece) {
        this.container.splice(this.container.indexOf(piece), 1);
    }
    isSafeFor(piece) {
        if (this.type == "start" || this.type == "homeRun" || this.type == "home" || this.container.length == 0) {
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

class Player {
    constructor(name, color) {
        this.color = color;
        this.name = name;

        this.pieceDict = {
            "green": [gp0, gp1, gp2, gp3],
            "yellow": [yp0, yp1, yp2, yp3],
            "red": [rp0, rp1, rp2, rp3],
            "blue": [bp0, bp1, bp2, bp3]
        };
        this.pieces = this.pieceDict[this.color];
        console.log(this.pieces[0].id);
        this.turn = false;

    }
    setActive(tossValue) {
        this.pieces.forEach((piece) => {
            this.addEventListener(piece, tossValue);
        });
        // for(var i=0;i<this.pieces.length;i++){
        //     let piece = this.pieces[i];
        //     console.log(piece.id);
        //     if(piece.cell == piece.station && tossValue==6){
        //         console.log(piece.dom);
        //         let id = piece.id;
        //         document.querySelector(id).addEventListener("click",()=>{if(this.turn==true){piece.enable();}});
        //     }
        //     else{

        //     }
        // }

    }
    addEventListener(piece, tossValue) {
        if (piece.cell == piece.station && tossValue == 6) {
            console.log(piece.dom);
            let id = piece.id;
            document.querySelector(id).addEventListener("click", () => {
                if (this.turn == true) {
                    piece.enable();
                }
            });
        }
        else {
            if (piece.cell !== piece.station && tossValue < piece.path.length - piece.path.indexOf(piece.cell)) {

                
                document.querySelector(piece.id).removeEventListener("click", () => { this.moveToss(piece, tossValue) });
                document.querySelector(piece.id).addEventListener("click", () => { this.moveToss(piece, tossValue) });
            }

        }
    }

    moveToss(piece, tossValue) {
        if (this.turn == true) {
            getPiece(piece.id).nMove(tossValue);
            this.turn = false;
            // this = new Player(this.name,this.color);
            var red = new Player("abrham","red");
            var green = new Player("abrham","green");
            var blue = new Player("abrham","blue");
            var yellow = new Player("abrham","yellow");
        }
    };

    swapObject(){
        var red = new Player("abrham","red");
        var green = new Player("abrham","green");
        var blue = new Player("abrham","blue");
        var yellow = new Player("abrham","yellow");
       var objDict={
           "red":red,
           "green":green,
           "blue":blue,
           "yellow":yellow

       };



    }
}


class Dice {
    constructor() {
        this.value = 1;
        window.setTimeout(() => this.addEventListener(), 100);
        window.setTimeout(() => { this.dom = document.querySelector("#dice") }, 10);

    }

    sleep(milliseconds) {
        return new Promise(resolve => setTimeout(resolve, milliseconds));

    };
    toss() {
        var min = 1;
        var max = 6;
        var tossValue = Math.floor(Math.random() * (max - min + 1)) + min;

        this.value = tossValue;
        console.log(`random value ${this.value}`);
        this.display(0);
        return tossValue;
    }

    display(index) {
        var diceImages = [
            "./assets/images/3.png",
            "./assets/images/5.png",
            "./assets/images/1.png",
            "./assets/images/2.png",
            "./assets/images/4.png",
            "./assets/images/6.png"
        ];
        var dict = {
            3: 0,
            5: 1,
            1: 2,
            2: 3,
            4: 4,
            6: 5
        }
        var i = index;
        if (i == 6) {
            var dom = document.querySelector("#diceImg");
            window.setTimeout(() => { dom.src = diceImages[dict[this.value]]; }, 300);

        }
        else {
            this.sleep(300).then(() => {
                this.display(i + 1)
                this.changeImg(i);


            });

        }





    }
    changeImg(index) {
        var diceImages = [
            "./assets/images/3.png",
            "./assets/images/5.png",
            "./assets/images/1.png",
            "./assets/images/2.png",
            "./assets/images/4.png",
            "./assets/images/6.png"
        ];

        var dom = document.querySelector("#diceImg");
        dom.src = diceImages[index];
    }
    addEventListener() {
        var dom = document.querySelector("#diceImg");
        dom.addEventListener("click", () => { this.toss() });
        window.addEventListener("load", () => { this.place() });
        window.addEventListener("resize", () => { this.place() });

    }

    // place() {
    //     var dom = a23.dom;
    //     //   console.log(dom);
    //     this.dom.style.top = a23.dom.getBoundingClientRect().top + a23.dom.getBoundingClientRect().height + "px";
    //     this.dom.style.left = a23.dom.getBoundingClientRect().left + a23.dom.getBoundingClientRect().width / 2 + "px";
    //     this.dom.style.width = a23.dom.getBoundingClientRect().width * 2 + "px";
    //     document.querySelector("#diceImg").style.width = a23.dom.getBoundingClientRect().width * 2.5 + "px";
    //     //   console.log(this.dom.style.width);
    // }
    place() {
        var dom = a23.dom;
        //   console.log(dom);
        let rgby = document.querySelector("#rgby");
        this.dom.style.top = rgby.getBoundingClientRect().top+"px";
        this.dom.style.left = rgby.getBoundingClientRect().left+"px";
        // this.dom.style.width = a23.dom.getBoundingClientRect().width * 2 + "px";
        // document.querySelector("#diceImg").style.width = a23.dom.getBoundingClientRect().width * 2.5 + "px";
        //   console.log(this.dom.style.width);
    }

}


function getPiece(id) {
    var pieceId = {
        "#gp0": gp0,
        "#gp1": gp1,
        "#gp2": gp2,
        "#gp3": gp3,

        "#rp0": rp0,
        "#rp1": rp1,
        "#rp2": rp2,
        "#rp3": rp3,

        "#yp0": yp0,
        "#yp1": yp1,
        "#yp2": yp2,
        "#yp3": yp3,

        "#bp0": bp0,
        "#bp1": bp1,
        "#bp2": bp2,
        "#bp3": bp3
    };
    return pieceId[id];
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


rp0 = new Piece("#rp0", r7);
rp1 = new Piece("#rp1", r8);
rp2 = new Piece("#rp2", r9);
rp3 = new Piece("#rp3", r10);





gp0 = new Piece("#gp0", g7);
gp1 = new Piece("#gp1", g8);
gp2 = new Piece("#gp2", g9);
gp3 = new Piece("#gp3", g10);



bp0 = new Piece("#bp0", b7);
bp1 = new Piece("#bp1", b8);
bp2 = new Piece("#bp2", b9);
bp3 = new Piece("#bp3", b10);


yp0 = new Piece("#yp0", y7);
yp1 = new Piece("#yp1", y8);
yp2 = new Piece("#yp2", y9);
yp3 = new Piece("#yp3", y10);


dice = new Dice();

var red = new Player("abrham","red");
var green = new Player("abrham","green");
var blue = new Player("abrham","blue");
var yellow = new Player("abrham","yellow");
// function placeAtStation() {
//     var piecesArray = [rp0, rp1, rp2, rp3, gp0, gp1, gp2, gp3, bp0, bp1, bp2, bp3, yp0, yp1, yp2, yp3];
//     piecesArray.forEach((piece) => { { if (piece.cell !== piece.station) { } else { piece.placeAtStation(); } } });
// }

// window.setTimeout(() => placeAtStation(), 105);
// window.addEventListener("resize", () => placeAtStation());`