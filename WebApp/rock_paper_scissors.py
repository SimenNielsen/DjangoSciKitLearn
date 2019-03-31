from sklearn import svm
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pickle
import pandas
from joblib import dump, load
import numpy as np
from sklearn import datasets

# Computer num, player num, result (Even, Win(Computer), Lost(Computer))
def generate_first():
    num_games = 1
    dataset = np.random.random_integers(0,2,num_games*2)
    dataset.shape = (num_games, 2)
    results = []
    for data in dataset:
        results.append(process_game(data))    
    #dataset = np.append(dataset, results, axis = 1)
    
    #knn = KNeighborsClassifier(n_neighbors=1)
    dataset = np.c_[dataset, results]
    #X = dataset[:,1:3] 
    #y = dataset[:,0]
    #knn.fit(X, y)
    return dataset

def process_game(data):
    if data[0] == data[1]:
        return 0
    elif (data[0] == 0 and data[1] == 2) or (data[0] == 1 and data[1] == 0) or (data[0] == 2 and data[1] == 1):
        return 1
    elif (data[0] == 0 and data[1] == 1) or (data[0] == 1 and data[1] == 2) or (data[0] == 2 and data[1] == 0):
        return 2
    return None

def play_RPS(turn_order,human_choice):
    human_choice = int(human_choice)
    data_path = 'sklearn/data/rps.csv'
    try:
        dataset = np.loadtxt(data_path, delimiter=',', dtype='int')
        print(int(len(dataset)/3))
        dataset.shape = (int(len(dataset/3)), 3)
        print('reading from file')
    except:
        dataset = generate_first()
        dataset.shape = (1, 3)
        print('generating')
    knn = KNeighborsClassifier(n_neighbors=1)
    if turn_order == 'human':
        X = dataset[:,1:3] 
        y = dataset[:,0]
        knn.fit(X, y)
        prediction = knn.predict([[human_choice,1]])[0]
    elif turn_order == 'computer':
        X = dataset[:,2:3] 
        y = dataset[:,1]
        knn.fit(X, y)
        prediction = knn.predict([[1]])[0]
    elif turn_order == 'both':
        X = dataset[:,2:3] 
        y = dataset[:,1]
        knn.fit(X, y)
        prediction = knn.predict([[1]])[0]
    else:
        print('/////////////ERROR//////////////')
    print(dataset)
    dataset = np.append(dataset, [[prediction, human_choice, process_game([prediction, human_choice])]], axis=0)
    np.savetxt(data_path, dataset.astype(int), fmt='%i', delimiter=",")
    return prediction