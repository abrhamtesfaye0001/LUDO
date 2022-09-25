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


class Player{
    constructor(color){
        this.color = color;
    }
}

export {Piece,Cell,Player};