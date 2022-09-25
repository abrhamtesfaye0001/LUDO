from objects import *
import numpy as np
def availablePieces(pieceList,tossValue):
    freePieces = []
    for piece in pieceList:
        if(piece.ableToMoveWith(tossValue)):
            freePieces.append(piece)
    return freePieces




def getPlayerState(turn):
    state = []
    color  =  ["red", "green", "yellow", "blue"][turn]
    # print("=======================================")
    # print(color)
    progress = 0
    pathLength=len(path[f"{color}Path"])
    for piece in pieces[turn]:
        progress+= piece.value
        # print(piece)
        
        # print(len(playerPath))
        # print(piece.cell)
        # print(playerPath)
        # print(playerPath[0])
        
        if(piece.cell.cellType=="station"):
            piece_state = [-1000 for i in range(12)]
            piece_state.insert(6,0)
            # print(piece_state)
            
        else:
            piecePosition = 0
            colorPath = path[f"{color}Path"]
            pathLength = len(colorPath)
            for i in range(pathLength):
                if(colorPath[i]==piece.cell):
                    piecePosition=i
                    break
            if (piece.cell.cellType in ["start" , "open"] ):
                piece_state = []
                # print(piecePosition)
                if(piecePosition not in range(0,7)):
                    for cellIndex in [i+piecePosition if i + piecePosition < pathLength else pathLength-i + piecePosition for i in range(-6,7)]:
                        # print(cellIndex,"  out of ",pathLength)
                        cellPoint = 0
                        for cellOccupant in colorPath[cellIndex].container:
                            if(piece != cellOccupant and cellOccupant.color != piece.color):
                                if(cellIndex > piecePosition):
                                    cellPoint += cellOccupant.value 
                                else:
                                    cellPoint -= cellOccupant.value
                            elif (piece == cellOccupant):
                                if(piece.color == cellOccupant.color):
                                    cellPoint += cellOccupant.value 
                                else:
                                    cellPoint -= cellOccupant.value 
                            
                        piece_state.append(cellPoint)
                else:
                    # edgePath
                    prevCells = [edgePath[f"{color}Path"][piecePosition+6+i] for i in range(-6,1)]
                    # prevCells.reverse()
                    nextCells = [colorPath[i] for i in range(piecePosition+1,piecePosition+7)]
                    edgeCells = prevCells+nextCells
                    # for cell in edgeCells:
                    #     print(cell.id, end=" => ")
                    # print(len(prevCells),"--",len(nextCells))
                    for cellIndex in range(len(edgeCells)):
                        cellPoint = 0
                        for cellOccupant in edgeCells[cellIndex].container:
                            if(piece != cellOccupant and cellOccupant.color != piece.color):
                                if(cellIndex > piecePosition+6):
                                    cellPoint += cellOccupant.value  
                                else:
                                    cellPoint -= cellOccupant.value 
                        piece_state.append(cellPoint)

                # state.append(piece_state)
                # print(piece_state)


                
            else:
                piece_state = [0 if i + piecePosition < pathLength else -1000 for i in range(-6,7)]
                # print([0 if i + piecePosition < pathLength else float("-inf") for i in range(-6,7)])
        safeCellTypes = ["home","homeRun","station","swiss"]
        if(piece.cell.cellType in safeCellTypes):
            piece_state.append(1)
        else:
            piece_state.append(0)
        state+=piece_state
        # state.append(dice.getValue())
        
        
        # for state in state:
        #     print(state)
    # print(f"======================================={color} => {100*(progress/ (4*pathLength))}% ")
    # print(state)
    return state
            
if __name__=="__main__":
    getPlayerState(0)








