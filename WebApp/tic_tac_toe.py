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
        train_history = []
        result_history = []
        for i in range(0,num):
            history = []
            while True:
                history.append(self.get_random_move(history))
                if self.check_game_finish(history):
                    break
            winner = self.get_result(history)
            train_history.append(history)
            result_history.append(winner)
            print(i)
        dataset = np.c_[np.array(train_history, dtype=object), np.array(result_history, np.int32)]
        self.save_TTT_data(dataset)
        return
            
    def get_random_move(self, history):
        x = random.randint(1,3)
        y = random.randint(1,3)
        pos = str(x) + str(y)
        if pos in history:
            pos = self.get_random_move(history)
        return pos
        
    def check_game_finish(self, history):
        if len(history) > 8:
            return True
        c_history = history[1::2]
        p_history = history[0::2]
        if self.check_if_won(c_history):
            return True
        elif self.check_if_won(p_history):
            return True
        else:
            return False
        
    def check_if_won(self, history):
        for possible_h in self.possible_win_histories:
            if set(possible_h).issubset(history):
                return True
        return False
    
    def get_result(self, history):
        c_history = history[1::2]
        p_history = history[0::2]
        if self.check_if_won(c_history):
            return 2
        elif self.check_if_won(p_history):
            return 3
        else:
            return 1
    
    def get_TTT_data(self):
        try:
            dataset = np.loadtxt(self.data_path, delimiter=';', dtype='int')
            dataset.shape = (int(len(dataset/2)), 2)
            print('reading from file')
        except:
            dataset = self.train(100)
            dataset.shape = (int(len(dataset/2)), 2)
            print('generating')
        return dataset

    def save_TTT_data(self, dataset):
        np.savetxt(self.data_path,X=dataset, fmt=['%s','%i'], delimiter=";")
        