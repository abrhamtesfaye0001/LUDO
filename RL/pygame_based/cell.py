import random
from time import sleep
import pygame
from pygame.locals import *
from pygameObjects import *


class Cell:
    def __init__(self, id, cellType, x, y):
        self.id = id
        self.cellType = cellType
        self.container = []
        self.x = (x - 1) * 40
        self.y = (y - 1) * 40
        self.rect: Rect = Rect(self.x, self.y, 40, 40)
        # self.draw()
    

    def draw(self):
        # print(self.cellType)
        color = (0, 0, 0)
        if (self.cellType == "open"):
            color = (125, 125, 125)
        elif (self.id[0] == "r"):
            color = (255, 0, 0)
        elif (self.id[0] == "g"):
            color = (0, 255, 0)
        elif (self.id[0] == "b"):
            color = (0, 0, 255)
        elif (self.id[0] == "y"):
            color = (255, 255, 0)
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)

    def isClicked(self, eventPos):
        return self.rect.collidepoint(eventPos)

    def addPiece(self, piece):
        try:
            piece.cell.removePiece(piece)
        except:
            tst = 1
            # print("initial add")
        if (self.isSafeFor(piece)):
            # print("safe move")
            self.container.append(piece)
            piece.cell = self
            # print(self.container)

            piece.draw()
            return "safe"
        else:
            # print("not safe")

            for i in range(len(self.container)):
                i = 0
                self.container[i].reset()
            self.container.append(piece)
            piece.cell = self
            piece.draw()

            return "reset"

    def removePiece(self, piece):
        # print("++++++++++++++++++++++++++++++++")
        # print(self.container[0].id)
        self.container.pop(self.container.index(piece))
        # print(self.container)
        # print("++++++++++++++++++++++++++++++++")
        # self.container.remove(piece)

    def isSafeFor(self, piece):
        if (
                self.cellType == "start" or
                self.cellType == "homeRun" or
                self.cellType == "home" or
                len(self.container) == 0
        ):
            return True
        else:
            for discoveredPiece in self.container:
                if (discoveredPiece.color != piece.color):
                    return False
            return True

    def __eq__(self, o):
        return self.id == o.id

    def __str__(self):
        return str({"id": self.id, "cellType": self.cellType, "container": list(map(str, self.container))})


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
