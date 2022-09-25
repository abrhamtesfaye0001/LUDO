import random
from time import sleep
import time
import pygame
from pygame.locals import *
from pygameObjects import *

class Dice:

    def __init__(self):
        self.reRoll = True
        self.tossSpent = True
        
        self.__value = 1
        

        self.img = pygame.image.load("./images/dice-generic.jpg").convert()
        self.pos = ((8-1)*40,(8-1)*40)
        # self.isClicked((10,10))

    def reset(self):
        self.reRoll = True
        self.tossSpent = True
        self.__value = 1
        self.img = pygame.image.load("./images/dice-generic.jpg").convert()
        self.pos = ((8-1)*40,(8-1)*40)

    def getValue(self):
        return self.__value
    def roll(self):
        
        pygame.image.save(screen,f"./screenshots/{time.time()}.png")
        if(self.tossSpent):
            if(self.reRoll):
                self.tossSpent = False
                self.__value = random.randint(1, 6)
                print(f"dice rolled to {self.__value}")
                if(self.__value in [1,6]):
                    self.reRoll = True
                
                self.__rollAnimate()
                return self.__value
            else:
                return self.__value
        elif (self.reRoll):
            self.__value = random.randint(1, 6)
            return self.__value
        return  self.__value
    def __rollAnimate(self):
        images = ["./images/1.png","./images/2.png","./images/3.png","./images/4.png","./images/5.png","./images/6.png"]
        for img in images:
            self.img = pygame.image.load(img).convert()
            pygame.display.update((self.pos[0],self.pos[1],40,40))
            self.draw()
            # sleep(0.2)
        print(self.__value)
        pygame.display.update((self.pos[0],self.pos[1],40,40))
        self.img = pygame.image.load(images[self.__value-1]).convert()
        self.draw()
        pygame.display.update((self.pos[0],self.pos[1],40,40))

            
    def isClicked(self, eventPos):
        return pygame.Rect(self.pos[0],self.pos[1],40,40).collidepoint(eventPos)

    def draw(self):
        
        self.img = pygame.transform.scale(self.img,(40,40))
        screen.blit(self.img, self.pos)
    
    def is_a_ticket(self):
        return self.__value in [1,6]

