from time import sleep
from cell import Cell

from termcolor import colored


class Piece():
    def __init__(self, id: str, station: Cell, path: list):
        super().__init__()
        self.id = id
        self.station: Cell = station
        self.cell: Cell = station
        self.active = False
        self.atStation = True
        self.color = self.__getColor(self.id)
        self.path = path
        self.code = self.represent(self.id)      
        self.station.addPiece(self)
        self.value = 0
        
        
    
    def isHome(self): 
        return self.cell.cellType=="home"    

    def __getColor(self, id: str) -> str:
        prefix = self.id[0]
        if prefix == "r":
            return "red"
        if prefix == "g":
            return "green"
        if prefix == "b":
            return "blue"
        if prefix == "y":
            return "yellow"

    def __str__(self):
        return "Piece( id:{}, station:{}, cell:{}, active:{}, atStation:{}, color:{} )".format(self.id, self.station.id,
                                                                                               self.cell.id,
                                                                                               self.active,
                                                                                               self.atStation,
                                                                                               self.color)
    def __repr__(self) -> str:
        return colored(f"Piece({self.id}) at {self.cell.id}",self.color)
    
    def represent(self, id):
        postfix = id[-1]
        if (postfix == "0"):
            return [0, 0, 0, 1]
        elif postfix == "1":
            return [0, 0, 1, 0]
        elif postfix == "2":
            return [0, 1, 0, 0]
        else:
            return [1, 0, 0, 0]

    def nMove(self, tossValue: int) -> dict:
        if self.cell == self.station:
            if (tossValue == 1 or tossValue == 6):
                self.__enable()
                self.value += 1
                return {"tossSpent": True, "reRoll": True,"hasCutPiece": False}
            
            return {"tossSpent": False, "reRoll": False,"hasCutPiece": False}
        else:
            indexOfParentCell = self.path.index(self.cell)
            goalIndex = indexOfParentCell + tossValue
            # exceeds home
            if (indexOfParentCell > len(self.path) - 1 - tossValue):
                if (tossValue in [1,6] ):
                    return {"tossSpent": False, "reRoll": True, "hasCutPiece": False}
                return {"tossSpent": False, "reRoll": False, "hasCutPiece": False}
            else:
                # reaches home
                if (self.path[indexOfParentCell + tossValue].cellType == "home"):
                    self.path[indexOfParentCell + tossValue].addPiece(self)
                    self.value += tossValue
                    return {"tossSpent": True, "reRoll": True, "hasCutPiece": False}
                # normal move
                if (tossValue == 1 or tossValue == 6):
                    self.path[indexOfParentCell + tossValue].addPiece(self)
                    self.value += tossValue
                    return {"tossSpent": True, "reRoll": True, "hasCutPiece": False}
                # print("add piece ------------------->")
                if (self.path[indexOfParentCell + tossValue].cellType == "home"):
                    # if the piece has reached home
                    self.value += tossValue
                    return {"tossSpent": True, "reRoll": True, "hasCutPiece": False}
                else:
                    cutPieceReward = {"pieceValueCut":0,"pieceColorCut":""}
                    
                    for piece in self.path[indexOfParentCell + tossValue].container:
                            if(piece.color!=self.color):
                                cutPieceReward["pieceValueCut"]+= piece.value
                                cutPieceReward["pieceColorCut"]=piece.color
                    # reroll depends on whether the piece has resetted other pieces or not
                    hasCutPiece = (
                        self.path[indexOfParentCell + tossValue].addPiece(self) == "reset")
                    # if (hasCutPiece):
                        
                    self.value += tossValue
                    return {"tossSpent": True, "reRoll": hasCutPiece, "hasCutPiece": hasCutPiece,"cutPieceReward":cutPieceReward}
                    # else:
                    #     return {"tossSpent": True, "reRoll": False, "hasCutPiece": False}

    def ableToMoveWith(self, tossValue: int) -> bool:

        if (self.cell == self.station):
            if (tossValue == 1 or tossValue == 6):
                return True
            else:
                return False
        else:
            indexOfParentCell = self.path.index(self.cell)
            if (indexOfParentCell > len(self.path) - 1 - tossValue):
                return False
            else:
                return True

    def isAtStation(self) -> bool:
        return self.cell == self.station

    

    def __enable(self) -> None:
        self.active = True
        self.atStation = False
        self.path[0].addPiece(self)

    def reset(self) -> None:
        self.station.addPiece(self)
        self.active = False
        self.atStation = True
        self.value = 0

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return self.id == other.id
