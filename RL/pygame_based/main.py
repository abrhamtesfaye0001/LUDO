import random
from time import sleep
import pygame
from pygame.locals import *
from dice import Dice
from cell import Cell
from helper_methods import getPlayerState
from piece import Piece
from objects import *



def playerFreePieces(pieceList,tossValue):
    freePieces = []
    for piece in pieceList:
        if(piece.ableToMoveWith(tossValue)):
            freePieces.append(piece)
    return freePieces



turn = 0
turnUsed = False
numPlayers = 4

while True:
    pygame.display.set_caption(piecesName[turn])
    clock.tick(15)
    drawAll()
    # sprites.draw(screen)
    dice.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if(dice.tossSpent==False):
                # adapts with every turn/ player
                for piece in pieces[turn]:
                    if (piece.isClicked(event.pos)):
                        result = piece.nMove(dice.getValue())
                        # print(result)
                        dice.tossSpent = result["tossSpent"]
                        dice.reRoll = result["reRoll"]
                        # print(result)
                        getPlayerState("green")
                        if (dice.tossSpent and dice.reRoll==False)  and (result["hasCutPiece"] == False) :
                            turnUsed = True
                            dice.reRoll = True#dice reroll for the next turn
                        # introduce turn pass for unavailable moving pieces using turn used
                        break



            else:
                if(dice.reRoll==True):
                    if(dice.isClicked(event.pos)):
                        dice.roll()
                        availablePieces = playerFreePieces(pieces[turn],dice.getValue())
                        if(len(availablePieces)==0):
                            # if((dice.getValue()==1 or dice.getValue()==6)):#player is at home

                            turnUsed = True
                            dice.tossSpent = True
                            dice.reRoll = True
                            print("no pieces to move")



    if(turnUsed):
        availablePieces = playerFreePieces(pieces[turn],1)
        if(len(availablePieces)==0):
            pieces.pop(turn)
            turnUsed = False
            numPlayers=-1
            # print(f"number of players is now ${numPlayers}")

        else:
            turn = (turn+1)%numPlayers
            turnUsed = False








"""
actions
------------------------
[0,0,0,1] piece0
[0,0,1,0] piece1
[0,1,0,0] piece2
[1,0,0,0] piece3

reward
------------------------
takoutPiece +10
losePiece -10
getHome +20
else 0


state
-------------------
dangerBehind
preyInfront
home

"""
