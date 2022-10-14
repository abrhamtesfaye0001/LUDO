import random

class Dice:

    def __init__(self):
        self.reRoll = True
        self.tossSpent = True
        
        self.__value = 1

    def reset(self):
        self.reRoll = True
        self.tossSpent = True
        self.__value = 1
        self.pos = ((8-1)*40,(8-1)*40)

    def getValue(self):
        return self.__value
    def roll(self):
        if(self.tossSpent):
            if(self.reRoll):
                self.tossSpent = False
                self.__value = random.randint(1, 6)
                print(f"dice rolled to {self.__value}")
                if(self.__value in [1,6]):
                    self.reRoll = True
                return self.__value
            else:
                return self.__value
        elif (self.reRoll):
            self.__value = random.randint(1, 6)
            return self.__value
        return  self.__value
    def is_a_ticket(self):
        return self.__value in [1,6]

