class Board{
    constructor(){
        

    }






}



class node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
    addNext(next){
        this.next = next;
    }
}

class CircularLinkedList{
    constructor(start){//input node object
        this.start = start;
        this.end = null;
    }

    addNext(end){//input node object
        if (this.end==null){//first time end
            this.start.addNext(end);
        }
        else{
            this.end.addNext(end);
        }
    }

    get(value,startingPosition){//input node object
        if (startingPosition.next!=this.start){// prevent deep recursion to stop at start
            if (value==startingPosition){
                return startingPosition;
            }
            else{
                get(value,startingPosition.next);
            }
        }else{
            return null;
        }
        
    }

}