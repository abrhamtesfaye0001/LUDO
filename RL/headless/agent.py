import torch
import random
import numpy as np
from collections import deque
# from game import *
from model import Linear_QNet, QTrainer
from helper_methods import *
from model import *
from math import *
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self,player_turn) -> None:
        self.player_turn = player_turn
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = Linear_QNet(57,512,4)
        self.trainer = QTrainer(self.model,lr=LR,gamma=self.gamma)

    def get_state(self,game):
        # print(game.get_state())
        return np.array(game.get_state(),dtype=int)
    
    def remember(self,state,action,reward,next_state,done):
        self.memory.append((state,action,reward,next_state,done))
        
        
    def get_action(self,state):
        # 80
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0,0]
        
        if random.randint(0,200) < self.epsilon:
            move = random.randint(0,3)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state,dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
        # print(availablePieces(pieces[self.player_turn],state[-1]))
        # //////////////////////////
        # freePieceIndices = np.array([0,0,0,0])
        # for piece in availablePieces(pieces[self.player_turn],state[-1]):
        #     freePieceIndices+=np.array(piece.represent(piece.id))
        #     # print(piece.id,"==>",self.player_turn)
        # print(freePieceIndices)
        # nonFreeIndices = []
        # for i in range(len(freePieceIndices)):
        #     if(freePieceIndices[i]==0):
        #         nonFreeIndices.append(i)
        # print(move)
        # for j in range(len(nonFreeIndices)):
        #     if(move in nonFreeIndices):
        #         print(freePieceIndices,nonFreeIndices)
        #         prediction[move] = 0
        #         move = torch.argmax(prediction).item()
        #         # print(prediction)
        #     else:
        #         break
        # //////////////////////////
        print(move)
        
        final_move[move] = 1
        
        return final_move

    def train_short_memory(self,state,action,reward,next_state,done):
        return self.trainer.train_step(state,action,reward,next_state,done)
    
    def train_long_memory(self):
        if(len(self.memory)>BATCH_SIZE):
            mini_sample = random.sample(self.memory,BATCH_SIZE)
        else:
            mini_sample = self.memory
        
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states,actions,rewards,next_states,dones)
    def getProgress(self,game):
        return game.progress(self.player_turn)

