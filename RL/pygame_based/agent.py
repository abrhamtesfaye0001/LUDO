import torch
import random
import numpy as np
from collections import deque
# from game import *
from model import Linear_QNet, QTrainer
from helper_methods import *
from model import *

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
        self.model = Linear_QNet(57,1024,4)
        self.trainer = QTrainer(self.model,lr=LR,gamma=self.gamma)

    def get_state(self,game):
        # print(game.get_state())
        return np.array(game.get_state(),dtype=int)
    
    def remember(self,state,action,reward,next_state,done):
        self.memory.append((state,action,reward,next_state,done))
        
        
    def get_action(self,state):
        # 80
        self.epsilon = 80 - self.n_games

        self.n_games+=1
        
        final_move = [0,0,0,0]
        if random.randint(0,200) < self.epsilon:
            move = random.randint(0,3)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state,dtype=torch.float)
            prediction = self.model(state0)
            print(prediction)
            move = torch.argmax(prediction).item()
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




    
    






# def train():
#     global turn

#     agent0 = Agent(0)
#     agent1 = Agent(1)
#     agent2 = Agent(2)
#     agent3 = Agent(3)
#     agents = [agent0,agent1,agent2,agent3]
#     game = LudoGame("gameid134")



#     while True:

#         # pygame.display.set_caption(piecesName[turn])
#         clock.tick(15)
#         drawAll()

#         # sprites.draw(screen)
#         dice.draw()
#         pygame.display.flip()
#         # agent.get_state(game)
#         currentAgent = agents[turn]
        
        


#         state_old = currentAgent.get_state(game)
#         final_move = currentAgent.get_action(state_old)
#         # print(final_move)
#         reward, done, score = game.play_step(final_move.index(1))
#         print(f"score==={colors[turn]}=====> {score}")
#         state_new = currentAgent.get_state(game)
#         print(turn)
        
#         currentAgent.train_short_memory(state_old,final_move,reward, state_new,done)
#         currentAgent.remember(state_old,final_move,reward, state_new,done)
#         if done:
#             game.reset()
#             currentAgent.n_games+=1
#             print(f"game => {currentAgent.n_games}")

#         # game.play_step(1)
# class Logger(object):
#     def __init__(self, filename="Default.log"):
#         self.terminal = sys.stdout
#         self.log = open(filename, "a")

#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)

# if __name__=='__main__':
#     # with open("file","a") as sys.stdout:
#     #     train()
#     sys.stdout = Logger("gameLogger.txt")
#     train()












