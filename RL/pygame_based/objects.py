import random
from time import sleep
import pygame
from pygame.locals import *
from dice import Dice
from cell import Cell
from piece import Piece
from pygameObjects import *




a0 = Cell("a0", "open", 9, 3)
a1 = Cell("a1", "open", 9, 4)
a2 = Cell("a2", "open", 9, 5)
a3 = Cell("a3", "open", 9, 6)
a4 = Cell("a4", "open", 10, 7)
a5 = Cell("a5", "open", 11, 7)
a6 = Cell("a6", "open", 12, 7)
a7 = Cell("a7", "open", 13, 7)
a8 = Cell("a8", "open", 14, 7)
a9 = Cell("a9", "open", 15, 7)
a10 = Cell("a10", "open", 15, 8)
a11 = Cell("a11", "open", 15, 9)
a12 = Cell("a12", "open", 13, 9)
a13 = Cell("a13", "open", 12, 9)
a14 = Cell("a14", "open", 11, 9)
a15 = Cell("a15", "open", 10, 9)
a16 = Cell("a16", "open", 9, 10)
a17 = Cell("a17", "open", 9, 11)
a18 = Cell("a18", "open", 9, 12)
a19 = Cell("a19", "open", 9, 13)
a20 = Cell("a20", "open", 9, 14)
a21 = Cell("a21", "open", 9, 15)
a22 = Cell("a22", "open", 8, 15)
a23 = Cell("a23", "open", 7, 15)
a24 = Cell("a24", "open", 7, 13)
a25 = Cell("a25", "open", 7, 12)
a26 = Cell("a26", "open", 7, 11)
a27 = Cell("a27", "open", 7, 10)
a28 = Cell("a28", "open", 6, 9)
a29 = Cell("a29", "open", 5, 9)
a30 = Cell("a30", "open", 4, 9)
a31 = Cell("a31", "open", 3, 9)
a32 = Cell("a32", "open", 2, 9)
a33 = Cell("a33", "open", 1, 9)
a34 = Cell("a34", "open", 1, 8)
a35 = Cell("a35", "open", 1, 7)
a36 = Cell("a36", "open", 3, 7)
a37 = Cell("a37", "open", 4, 7)
a38 = Cell("a38", "open", 5, 7)
a39 = Cell("a39", "open", 6, 7)
a40 = Cell("a40", "open", 7, 6)
a41 = Cell("a41", "open", 7, 5)
a42 = Cell("a42", "open", 7, 4)
a43 = Cell("a43", "open", 7, 3)
a44 = Cell("a44", "open", 7, 2)
a45 = Cell("a45", "open", 7, 1)
a46 = Cell("a46", "open", 8, 1)
a47 = Cell("a47", "open", 9, 1)

r0 = Cell("r0", "start", 9, 2)
r1 = Cell("r1", "homeRun", 8, 2)
r2 = Cell("r2", "homeRun", 8, 3)
r3 = Cell("r3", "homeRun", 8, 4)
r4 = Cell("r4", "homeRun", 8, 5)
r5 = Cell("r5", "homeRun", 8, 6)
r6 = Cell("r6", "home", 8, 7)
r7 = Cell("r7", "station", 12, 3)
r8 = Cell("r8", "station", 13, 3)
r9 = Cell("r9", "station", 13, 4)
r10 = Cell("r10", "station", 12, 4)

g0 = Cell("g0", "start", 2, 7)
g1 = Cell("g1", "homeRun", 2, 8)
g2 = Cell("g2", "homeRun", 3, 8)
g3 = Cell("g3", "homeRun", 4, 8)
g4 = Cell("g4", "homeRun", 5, 8)
g5 = Cell("g5", "homeRun", 6, 8)
g6 = Cell("g6", "home", 7, 8)
g7 = Cell("g7", "station", 3, 3)
g8 = Cell("g8", "station", 4, 3)
g9 = Cell("g9", "station", 4, 4)
g10 = Cell("g10", "station", 3, 4)

b0 = Cell("b0", "start", 14, 9)
b1 = Cell("b1", "homeRun", 9, 8)
b2 = Cell("b2", "homeRun", 10, 8)
b3 = Cell("b3", "homeRun", 11, 8)
b4 = Cell("b4", "homeRun", 12, 8)
b5 = Cell("b5", "homeRun", 13, 8)
b6 = Cell("b6", "home", 14, 8)
b7 = Cell("b7", "station", 12, 12)
b8 = Cell("b8", "station", 13, 12)
b9 = Cell("b9", "station", 13, 13)
b10 = Cell("b10", "station", 12, 13)

y0 = Cell("y0", "start", 7, 14)
y1 = Cell("y1", "homeRun", 8, 14)
y2 = Cell("y2", "homeRun", 8, 13)
y3 = Cell("y3", "homeRun", 8, 12)
y4 = Cell("y4", "homeRun", 8, 11)
y5 = Cell("y5", "homeRun", 8, 10)
y6 = Cell("y6", "home", 8, 9)
y7 = Cell("y7", "station", 3, 12)
y8 = Cell("y8", "station", 4, 12)
y9 = Cell("y9", "station", 4, 13)
y10 = Cell("y10", "station", 3, 13)

path = {

    "redPath": [r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20,
                a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39,
                a40, a41, a42, a43, a44, a45, a46, r1, r2, r3, r4, r5, r6],
    "greenPath": [g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7,
                  a8, a9, a10, a11, b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26,
                  a27, a28, a29, a30, a31, a32, a33, a34, g1, g2, g3, g4, g5, g6],
    "bluePath": [b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, y0, a24, a25, a26, a27, a28, a29, a30,
                 a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, r0, a0, a1,
                 a2, a3, a4, a5, a6, a7, a8, a9, a10, b1, b2, b3, b4, b5, b6],
    "yellowPath": [y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, g0, a36, a37, a38, a39, a40, a41,
                   a42, a43, a44, a45, a46, a47, r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, b0, a12, a13,
                   a14, a15, a16, a17, a18, a19, a20, a21, a22, y1, y2, y3, y4, y5, y6]

}

publicPath= [r0, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, 
               b0, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
               y0, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, 
               g0, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47]
publicPathLength = len(publicPath)

_redStartCellIndex = 0
_greenStartCellIndex = 0
_blueStartCellIndex = 0
_yellowStartCellIndex = 0

for cellIndex in range(publicPathLength):
    cell = publicPath[cellIndex]
    if(cell.id.startswith("r")):
        _redStartCellIndex = cellIndex
    if(cell.id.startswith("g")):
        _greenStartCellIndex = cellIndex
    if(cell.id.startswith("b")):
        _blueStartCellIndex = cellIndex
    if(cell.id.startswith("y")):
        _yellowStartCellIndex = cellIndex



# edgePath = {
#     "redPath":[a42,a43,a44,a45,a46,a47,r0,a0,a1,a2,a3,a4,a5],
#     "greenPath":[a30,a31,a32,a33,a34,a35,g0,a36,a37,a38,a39,a40,a41],
#     "bluePath":[a6,a7,a8,a9,a10,a11,b0,a12,a13,a14,a15,a16,a17],
#     "yellowPath":[a18,a19,a20,a21,a22,a23,y0,a24,a25,a26,a27,a28,a29],
# }

edgePath = {
    "redPath": [publicPath[i+_redStartCellIndex] if i + _redStartCellIndex < publicPathLength else publicPath[i+_redStartCellIndex - publicPathLength] for i in range(-6,7)],
    "greenPath": [publicPath[i+_greenStartCellIndex] if i + _greenStartCellIndex < publicPathLength else publicPath[i+_greenStartCellIndex - publicPathLength] for i in range(-6,7)],
    "bluePath":[publicPath[i+_blueStartCellIndex] if i + _blueStartCellIndex < publicPathLength else publicPath[i+_blueStartCellIndex - publicPathLength] for i in range(-6,7)],
    "yellowPath":[publicPath[i+_yellowStartCellIndex] if i + _yellowStartCellIndex < publicPathLength else publicPath[i+_yellowStartCellIndex - publicPathLength] for i in range(-6,7)]
}



rp0 = Piece("rp0", r7, path["redPath"])
rp1 = Piece("rp1", r8, path["redPath"])
rp2 = Piece("rp2", r9, path["redPath"])
rp3 = Piece("rp3", r10, path["redPath"])

gp0 = Piece("gp0", g7, path["greenPath"])
gp1 = Piece("gp1", g8, path["greenPath"])
gp2 = Piece("gp2", g9, path["greenPath"])
gp3 = Piece("gp3", g10, path["greenPath"])

bp0 = Piece("bp0", b7, path["bluePath"])
bp1 = Piece("bp1", b8, path["bluePath"])
bp2 = Piece("bp2", b9, path["bluePath"])
bp3 = Piece("bp3", b10, path["bluePath"])

yp0 = Piece("yp0", y7, path["yellowPath"])
yp1 = Piece("yp1", y8, path["yellowPath"])
yp2 = Piece("yp2", y9, path["yellowPath"])
yp3 = Piece("yp3", y10, path["yellowPath"])

pieceMap = {
    "red": [rp0, rp1, rp2, rp3],
    "green": [gp0, gp1, gp2, gp3],
    "blue": [bp0, bp1, bp2, bp3],
    "yellow": [yp0, yp1, yp2, yp3],
}


def ableToMovePieces(color: str, tossValue: int) -> list:
    ablePieces = []
    for piece in pieceMap[color]:
        if (piece.ableToMoveWith(tossValue)):
            ablePieces.append(piece)
    return list(map(lambda x: str(x), ablePieces))


# class YAwareGroup(pygame.sprite.Group):
#     def by_y(self, spr):
#         return spr.rect.top
#
#     def draw(self, surface):
#         sprites = self.sprites()
#         surface_blit = surface.blit
#         for spr in sorted(sprites, key=self.by_y):
#             self.spritedict[spr] = surface_blit(spr.image, spr.rect)
#         self.lostsprites = []


all_pieces_list = pygame.sprite.Group()
all_pieces_list.add(rp0, rp1, rp2, rp3, gp0, gp1, gp2, gp3,
                    bp0, bp1, bp2, bp3, yp0, yp1, yp2, yp3)
# all_pieces_list.add(rp1)
# all_pieces_list.add(rp2)
# all_pieces_list.add(rp3)
#
# all_pieces_list.add(gp0)
# all_pieces_list.add(gp1)
# all_pieces_list.add(gp2)
# all_pieces_list.add(gp3)
#
# all_pieces_list.add(bp0)
# all_pieces_list.add(bp1)
# all_pieces_list.add(bp2)
# all_pieces_list.add(bp3)
#
# all_pieces_list.add(yp0)
# all_pieces_list.add(yp1)
# all_pieces_list.add(yp2)
# all_pieces_list.add(yp3)


def drawAll():
    a0.draw()
    a1.draw()
    a2.draw()
    a3.draw()
    a4.draw()
    a5.draw()
    a6.draw()
    a7.draw()
    a8.draw()
    a9.draw()
    a10.draw()
    a11.draw()
    a12.draw()
    a13.draw()
    a14.draw()
    a15.draw()
    a16.draw()
    a17.draw()
    a18.draw()
    a19.draw()
    a20.draw()
    a21.draw()
    a22.draw()
    a23.draw()
    a24.draw()
    a25.draw()
    a26.draw()
    a27.draw()
    a28.draw()
    a29.draw()
    a30.draw()
    a31.draw()
    a32.draw()
    a33.draw()
    a34.draw()
    a35.draw()
    a36.draw()
    a37.draw()
    a38.draw()
    a39.draw()
    a40.draw()
    a41.draw()
    a42.draw()
    a43.draw()
    a44.draw()
    a45.draw()
    a46.draw()
    a47.draw()

    r0.draw()
    r1.draw()
    r2.draw()
    r3.draw()
    r4.draw()
    r5.draw()
    r6.draw()
    r7.draw()
    r8.draw()
    r9.draw()
    r10.draw()

    g0.draw()
    g1.draw()
    g2.draw()
    g3.draw()
    g4.draw()
    g5.draw()
    g6.draw()
    g7.draw()
    g8.draw()
    g9.draw()
    g10.draw()

    b0.draw()
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()

    y0.draw()
    y1.draw()
    y2.draw()
    y3.draw()
    y4.draw()
    y5.draw()
    y6.draw()
    y7.draw()
    y8.draw()
    y9.draw()
    y10.draw()

    # rp0.draw()
    # rp1.draw()
    # rp2.draw()
    # rp3.draw()
    #
    # gp0.draw()
    # gp1.draw()
    # gp2.draw()
    # gp3.draw()
    #
    #
    # bp0.draw()
    # bp1.draw()
    # bp2.draw()
    # bp3.draw()
    #
    # yp0.draw()
    # yp1.draw()
    # yp2.draw()
    # yp3.draw()

    # print("draw")

    all_pieces_list.update()
    all_pieces_list.draw(screen)


dice = Dice()

cells = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23,
         a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45,
         a46, a47, r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, g0, g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, b0, b1, b2,
         b3, b4, b5, b6, b7, b8, b9, b10, y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10]

redPieces = [rp0, rp1, rp2, rp3]
greenPieces = [gp0, gp1, gp2, gp3]
bluePieces = [bp0, bp1, bp2, bp3]
yellowPieces = [yp0, yp1, yp2, yp3]
pieces = [redPieces, bluePieces, yellowPieces, greenPieces]
piecesName = ["red", "blue", "yellow", "green"]
