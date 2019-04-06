from sklearn import svm
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pickle
import pandas
from joblib import dump, load
import numpy as np
from sklearn import datasets
import random

class TTT():
    data_path = 'sklearn/data/ttt.csv'
    
    possible_win_histories = [
        ["11", "21", "31"],
        ["12", "22", "32"],
        ["13", "23", "33"],

        ["11", "12", "13"],
        ["21", "22", "23"],
        ["31", "32", "33"],

        ["11", "22", "33"],
        ["13", "22", "31"],
    ]
    
    def train(self, num):
        num_games = num
        
        for i in range(0,num):
            game_finish = False
            history = []
            while game_finish == False:
                history.append(self.get_random_move(history))
                game_finish = self.check_game_finish(history)
            winner = self.get_result(history)
        return
            
    def get_random_move(self, history):
        x = random.randint(1,4)
        y = random.randint(1,4)
        pos = str(x) + str(y)
        if pos in history:
            pos = self.get_random_move(history)
        else:
            return pos
        
    def check_game_finish(self, history):
        if len(history) > 8:
            return True
        elif len(history) % 2 == 1: # Check player moves
            p_history = history[1::2]
            return self.check_if_won(p_history)
        else: #Check Computer moves
            c_history = history[0::2]
            return self.check_if_won(c_history)
        
    def check_if_won(self, history):
        for possible_h in possible_win_histories:
            if set(possible_h).issubset(history):
                return True
        return False
    
    def get_result(self, history):
        #stuff
        return