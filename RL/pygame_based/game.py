from enum import Enum
import random
from time import sleep
import time
import pygame
from pygame.locals import *
from dice import Dice
from cell import Cell
from agent import Agent
from helper import plot
from piece import Piece
from objects import *
from helper_methods import *
import numpy as np
import sys
from termcolor import colored

global turn
global turnUsed
global gameFinished
turn = 0
turnUsed = True
gameFinished = False

def nextTurn():
    global turn
    global turnUsed
    turn+=1
    turn = turn % 4
    turnUsed = True
    dice.tossSpent = True
    dice.reRoll = True
    # dice.roll()
    pygame.display.set_caption(piecesName[turn])



class Color(Enum):
    RED = 0
    BLUE = 1
    YELLOW = 2
    GREEN = 3

def gameIsFinished():
    global turn
    count = 0
    for piece in pieces[turn]:
        if(piece.isHome()):
            count+=1
    return count == 4

global colors
global rewards
global scores

colors = ["red","blue","yellow","green"]
rewards = [0,0,0,0]
scores = [0,0,0,0]



class LudoGame:
    def __init__(self,id) -> None:
        self.id = id
        # initial game setup pygame
        self.rewards = [0,0,0,0]
    
    def reset(self):
        for color_pieces in pieceMap:
            for piece in pieceMap[color_pieces]:
                piece.reset()
        dice.reset()
    
    def get_state(self):
        state = []
        # for piece in pieces[turn]:
        #     state+=getPlayerState(turn)
        # print(pieces[turn])
        state+=getPlayerState(turn)
        state.append(dice.getValue())      
        
        return state
    
    def play_step(self,action):
        print(f"ai chose {action}")
        
        # [0,0,0,0]
        global turn
        global turnUsed
        global gameFinished
        global scores
        global rewards
        global colors
        # pieces[turn][np.argmax(action)].nMove(dice.getValue())
        reward = 0
        
        if(turnUsed):
            print("turn used")
            dice.roll()
            turnUsed = False

        # test in place of action prediction
        # print("waiting for input")
        selectedPiece = pieces[turn][action]
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # f = open("./game_verbose.txt","a")
                
                
                if event.key == pygame.K_1:
                    # print(f"=======================   {pieces[turn][0].color}   {dice.getValue()} =======================")
                    # f.write(f"\n=======================   {pieces[turn][0].color}   {dice.getValue()} =======================\n")
                    # print(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    # f.write(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    selectedPiece = pieces[turn][0]
                    self.get_state()
                if event.key == pygame.K_2:
                    # print(f"=======================   {pieces[turn][0].color}   {dice.getValue()} =======================")
                    # f.write(f"\n=======================   {pieces[turn][0].color}   {dice.getValue()} =======================\n")
                    # print(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    # f.write(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    selectedPiece = pieces[turn][1]
                    self.get_state()
                if event.key == pygame.K_3:
                    # print(f"=======================   {pieces[turn][0].color}   {dice.getValue()} =======================")
                    # f.write(f"\n=======================   {pieces[turn][0].color}   {dice.getValue()} =======================\n")
                    # print(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    # f.write(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    selectedPiece = pieces[turn][2]
                    self.get_state()
                if event.key == pygame.K_4:
                    # print(f"=======================   {pieces[turn][0].color}   {dice.getValue()} =======================")
                    # f.write(f"\n=======================   {pieces[turn][0].color}   {dice.getValue()} =======================\n")
                    # print(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    # f.write(f"{pieces[turn][0].color}\n {pieces[turn][0].id} - {pieces[turn][0].cell.id} \n {pieces[turn][1].id} - {pieces[turn][1].cell.id} \n {pieces[turn][2].id} - {pieces[turn][2].cell.id} \n {pieces[turn][3].id} - {pieces[turn][3].cell.id}")
                    selectedPiece = pieces[turn][3]
                    self.get_state()
                
                # pygame.image.save(screen,f"./screenshots/{time.time()}.png")
                    
                # f.close()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("click")
                for pieceIndex in range(len(pieces[turn])):
                    if (pieces[turn][pieceIndex].isClicked(event.pos)):
                        selectedPiece = pieces[turn][pieceIndex]
                        print("piece clicked")
                        break
        availablePieceList = availablePieces(pieces[turn],dice.getValue())
        if(len(availablePieceList)==0):
            prevTurn = turn
            nextTurn()
            # return reward,gameFinished,prevTurn, 
            return 0,gameIsFinished(),scores[prevTurn]
        if(selectedPiece):
            if(dice.tossSpent==False):
                # adapts with every turn/ player
                # dice toss gets spent/not below
                
                    
                result = selectedPiece.nMove(dice.getValue())
                # print(result)
                dice.tossSpent = result["tossSpent"]
                dice.reRoll = result["reRoll"]
                # print(result)
                # playerState = getPlayerState(turn)

                if (dice.tossSpent):
                    if(result["hasCutPiece"] == True) :
                        dice.reRoll = True
                        dice.roll()
                        cutPieceIndex = colors.index(result["cutPieceReward"]["pieceColorCut"])
                        rewards[cutPieceIndex] = -1 * result["cutPieceReward"]["pieceValueCut"]
                        print(f"rewardList => {cutPieceIndex} ",rewards)
                        scores[turn]+=result["cutPieceReward"]["pieceValueCut"]
                        # reward, gameDone, score
                        return  result["cutPieceReward"]["pieceValueCut"], gameIsFinished(), scores[turn]

                    if(dice.reRoll):
                        dice.reRoll = True
                        dice.roll()
                        # reward
                        return 0,gameIsFinished(),scores[turn]
                    else:
                        prevTurn = turn
                        nextTurn()
                        # reward
                        return 0,gameIsFinished(),scores[prevTurn]       
                    
                else:
                    
                    availablePieceList = availablePieces(pieces[turn],dice.getValue())
                    print("available pieces => ",len(availablePieceList))
                    if(len(availablePieceList)==0):
                        prevTurn = turn
                        # turnUsed = True
                        nextTurn()
                        print("no pieces to move")
                        return 0,gameIsFinished(),scores[prevTurn]
                    # TODO: ??? punish for moving invalid piece move
                    return -1000,gameIsFinished(),scores[turn]
                    


                # introduce turn pass for unavailable moving pieces using turn used
                



            else:
                if(dice.reRoll==True):
                    dice.tossSpent = True
                    dice.roll()
                    availablePieceList = availablePieces(pieces[turn],dice.getValue())
                    if(len(availablePieceList)==0):
                        # if((dice.getValue()==1 or dice.getValue()==6)):#player is at home
                        # turnUsed = True
                        print("no pieces to move")
                        nextTurn()
                        return 0,gameIsFinished(),scores[turn]


                else:
                    # turnUsed = True
                    nextTurn()
                    return 0,gameIsFinished(),scores[turn]
    def progress(self,turn):
        progressVal = 0
        for piece in pieces[turn]:
            progressVal+=piece.value
        return progressVal
    
    
class Queue:
    def __init__(self):
        self.container = []
    def push(self,new_item):
        self.container.append(new_item)
        return new_item
    def pop(self):
        if(len(self.container)==0):
            return None
        return self.container.pop(0)
    def peek_head(self):
        if(len(self.container)==0):
            return None
        return self.container[0]
    def peek_tail(self):
        if(len(self.container)==0):
            return None
        return self.container[-1]



def train():
    global turn

    agent0 = Agent(0)
    agent1 = Agent(1)
    agent2 = Agent(2)
    agent3 = Agent(3)
    agents = [agent0,agent1,agent2,agent3]
    game = LudoGame("gameid134")

    plot_scores_0 = []
    plot_scores_1 = []
    plot_scores_2 = []
    plot_scores_3 = []
          



    while True:

        # pygame.display.set_caption(piecesName[turn])
        clock.tick(15)
        drawAll()
    
        # sprites.draw(screen)
        dice.draw()
        pygame.display.flip()
        # agent.get_state(game)
        currentAgent = agents[turn]
        
        


        state_old = currentAgent.get_state(game)
        final_move = currentAgent.get_action(state_old)
        # print(final_move)
        currTurn = turn
        reward, done, score = game.play_step(final_move.index(1))
        print(f"score === {colors[turn]} =====> {score}")
        state_new = currentAgent.get_state(game)
        print(turn)
        
        if(rewards[currTurn]!=0):
            reward = rewards[currTurn] + reward
            rewards[currTurn] = 0
        
        print(f"reward => {reward}")
        currentAgent.train_short_memory(state_old,final_move,reward, state_new,done)
        currentAgent.remember(state_old,final_move,reward, state_new,done)

        plot_scores_0.append(agent0.getProgress(game))
        plot_scores_1.append(agent1.getProgress(game))
        plot_scores_2.append(agent2.getProgress(game))
        plot_scores_3.append(agent3.getProgress(game))

        # plot([{"plotable":plot_scores_0,"color":"red"},{"plotable":plot_scores_1,"color":"blue"},{"plotable":plot_scores_2,"color":"yellow"},{"plotable":plot_scores_3,"color":"green"}])
        # print(plot_scores_0)

        if done:
            game.reset()
            currentAgent.n_games+=1
            print(f"game => {currentAgent.n_games}")
            currentAgent.model.save(f"model {currentAgent.player_turn}.pth")
            sys.exit()

        # game.play_step(1)
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

if __name__=='__main__':
    # with open("file","a") as sys.stdout:
    #     train()
    # sys.stdout = Logger("gameLogger.txt")
    
    train()






















