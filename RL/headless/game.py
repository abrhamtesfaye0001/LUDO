
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
from fixed_size_queue import FixedSizeQueue

global turn
global turnUsed
global gameFinished
global stat
turn = 0
turnUsed = True
gameFinished = False
init_stat = {
    "illegal moves": [0, 0, 0, 0],
    "wins": [0, 0, 0, 0],
    "cuts": [0, 0, 0, 0],
    "move count": 0
}
stat = init_stat


def nextTurn():
    global turn
    global turnUsed
    print(f"turn changed from {turn} to {(turn+1)%4}")
    turn += 1
    turn = turn % 4
    turnUsed = True
    dice.tossSpent = True
    dice.reRoll = True
    # dice.roll()


def gameIsFinished():
    global turn
    count = 0
    for piece in pieces[turn]:
        if (piece.isHome()):
            count += 1
    return count == 4


global colors
global rewards
global scores

colors = ["red", "blue", "yellow", "green"]
rewards = [0, 0, 0, 0]
scores = [0, 0, 0, 0]


class LudoGame:
    def __init__(self) -> None:
        self.rewards = [0, 0, 0, 0]

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
        state += getPlayerState(turn)
        state.append(dice.getValue())

        return state

    def play_step(self, action):
        # print(f"ai chose {action}")

        # [0,0,0,0]
        global turn
        global turnUsed
        global gameFinished
        global scores
        global rewards
        global colors
        global stat
        # pieces[turn][np.argmax(action)].nMove(dice.getValue())
        reward = 0

        if (turnUsed):
            # print("turn used")
            dice.roll()
            turnUsed = False

        # test in place of action prediction
        # print("waiting for input")
        selectedPiece = pieces[turn][action]

        availablePieceList = availablePieces(pieces[turn], dice.getValue())
        if (len(availablePieceList) == 0):
            prevTurn = turn
            print(f"no available pieces next turn ----------------> {turn}")
            nextTurn()
            # return reward,gameFinished,prevTurn,
            return 0, gameIsFinished(), scores[prevTurn]
        if (selectedPiece):

            if (dice.tossSpent == False):
                # adapts with every turn/ player
                # dice toss gets spent/not below

                result = selectedPiece.nMove(dice.getValue())
                # print(result)
                dice.tossSpent = result["tossSpent"]
                dice.reRoll = result["reRoll"]
                # print(result)
                # playerState = getPlayerState(turn)

                if (dice.tossSpent):
                    if (result["hasCutPiece"] == True):
                        print(colored("cut piece", "green"))
                        stat["cuts"][turn] += 1
                        dice.reRoll = True
                        dice.roll()
                        cutPieceIndex = colors.index(
                            result["cutPieceReward"]["pieceColorCut"])
                        rewards[cutPieceIndex] = -100 * \
                            result["cutPieceReward"]["pieceValueCut"]
                        # print(f"rewardList => {cutPieceIndex} ", rewards)
                        scores[turn] += result["cutPieceReward"]["pieceValueCut"]
                        # reward, gameDone, score
                        return result["cutPieceReward"]["pieceValueCut"]*100, gameIsFinished(), scores[turn]

                    if (dice.reRoll):
                        print(colored("reRoll", "green"))
                        prevDice = dice.getValue()
                        dice.reRoll = True
                        dice.roll()
                        # reward
                        return prevDice, gameIsFinished(), scores[turn]
                    else:
                        print(colored("no reRoll", "blue"))
                        prevDice = dice.getValue()
                        prevTurn = turn
                        nextTurn()
                        # reward
                        return prevDice, gameIsFinished(), scores[prevTurn]

                else:

                    availablePieceList = availablePieces(
                        pieces[turn], dice.getValue())
                    # print("available pieces => ", len(availablePieceList))
                    if (len(availablePieceList) == 0):
                        print(colored("no pieces to move", "yellow"))
                        prevTurn = turn
                        # turnUsed = True
                        nextTurn()
                        # print("no pieces to move")
                        return 0, gameIsFinished(), scores[prevTurn]

                    print(colored(f"invalid  piece tried to move {len(availablePieces(pieces[turn], dice.getValue()))}", "red"))
                    stat["illegal moves"][turn] += 1
                    # TODO: ??? punish for moving invalid piece move
                    return -1000, gameIsFinished(), scores[turn]

                # introduce turn pass for unavailable moving pieces using turn used

            else:
                if (dice.reRoll == True):
                    dice.tossSpent = True
                    dice.roll()
                    availablePieceList = availablePieces(
                        pieces[turn], dice.getValue())
                    if (len(availablePieceList) == 0):
                        # if((dice.getValue()==1 or dice.getValue()==6)):#player is at home
                        # turnUsed = True
                        print(colored("no pieces to move", "red"))
                        # print("no pieces to move")
                        nextTurn()
                        return 0, gameIsFinished(), scores[turn]

                else:
                    print(colored("no reRoll 2", "blue"))
                    prevDice = dice.getValue()
                    nextTurn()
                    return prevDice, gameIsFinished(), scores[turn]

        # print("/////////////////////// reached here")
        return 0, 0, scores[turn]

    def progress(self, turn):
        progressVal = 0
        for piece in pieces[turn]:
            progressVal += piece.value
        return progressVal


def train(epoch=10):
    global turn

    agent0 = Agent(0)
    agent1 = Agent(1)
    agent2 = Agent(2)
    agent3 = Agent(3)
    # agents = [agent0, agent1, agent2, agent3]
    agents = [agent0, agent0, agent0, agent0]
    game = LudoGame()

    plot_scores_0 = FixedSizeQueue(100)
    plot_scores_1 = FixedSizeQueue(100)
    plot_scores_2 = FixedSizeQueue(100)
    plot_scores_3 = FixedSizeQueue(100)

    currEpoch = 0
    while True:
        # print(f"game number {currEpoch}")
        currentAgent = agents[turn]
        
        state_old = currentAgent.get_state(game)
        final_move = currentAgent.get_action(state_old)
        # print(final_move)
        currTurn = turn
        reward, done, score = game.play_step(final_move.index(1))
        # print(f"score === {colors[turn]} =====> {score}")
        state_new = currentAgent.get_state(game)
        # print(turn)

        # punishments for being cut by the other players
        if (rewards[currTurn] != 0):
            reward = rewards[currTurn] + reward
            rewards[currTurn] = 0
        # reward wining the game massively
        if (done):
            stat["wins"][turn] += 1
            reward = 10000
        if (reward != -1000):
            stat["move count"] += 1
        else:
            #  print(stat)
            pass
        # print(f"reward => {reward}")
        currentAgent.train_short_memory(
            state_old, final_move, reward, state_new, done)
        currentAgent.remember(state_old, final_move, reward, state_new, done)

        plot_scores_0.push(agent0.getProgress(game))
        plot_scores_1.push(agent1.getProgress(game))
        plot_scores_2.push(agent2.getProgress(game))
        plot_scores_3.push(agent3.getProgress(game))

        

        plot([{"plotable": plot_scores_0.toList(), "color": "red"}, {"plotable": plot_scores_1.toList(), "color": "blue"}, {
             "plotable": plot_scores_2.toList(), "color": "yellow"}, {"plotable": plot_scores_3.toList(), "color": "green"}], 
             f"Training ... {sum(stat['wins'])}th game {stat['move count']}th move", 
             str(stat).replace("],", "],\n"))
        if(stat["move count"]%100==0):
            # print(f"progress => [{agent0.getProgress(game)},{agent1.getProgress(game)},{agent2.getProgress(game)},{agent3.getProgress(game)}]")
            print(f"stats => {str(stat)}")

        if done:
            game.reset()
            currEpoch += 1
            currentAgent.n_games += 1
            print(f"game => {currentAgent.n_games}")
            agent0.train_long_memory()
            # agent1.train_long_memory()
            # agent2.train_long_memory()
            # agent3.train_long_memory()
            currentAgent.model.save(f"model {currentAgent.player_turn}.pth")

            if (currEpoch > epoch):
                sys.exit()


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)


if __name__ == '__main__':
    # with open("file","a") as sys.stdout:
    #     train()
    # sys.stdout = Logger("gameLogger.txt")

    train()
