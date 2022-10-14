class Cell:
    def __init__(self, id, cellType, x, y):
        self.id = id
        self.cellType = cellType
        self.container = []
        


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
            return "safe"
        else:
            # print("not safe")

            for i in range(len(self.container)):
                i = 0
                self.container[i].reset()
            self.container.append(piece)
            piece.cell = self
           

            return "reset"

    def removePiece(self, piece):
        self.container.pop(self.container.index(piece))
        

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
