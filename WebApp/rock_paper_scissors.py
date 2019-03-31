from sklearn import svm
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pickle
import numpy as np
from sklearn import datasets

# Computer num, player num, result (Even, Win(Computer), Lost(Computer))
def generate_model():
    dataset = np.random.random_integers(0,2,1000)
    dataset.shape = (500, 2)
    results = []
    for data in dataset:
        results.append(process_game(data))    
    #dataset = np.append(dataset, results, axis = 1)
    
    knn = KNeighborsClassifier(n_neighbors=1)
    dataset = np.c_[dataset, results]
    X = dataset[:,1:3] 
    y = dataset[:,0]
    knn.fit(X, y)
    print(knn.predict([[0,1]]))
    return

def process_game(data):
    if data[0] == data[1]:
        return 0
    elif (data[0] == 0 and data[1] == 2) or (data[0] == 1 and data[1] == 0) or (data[0] == 2 and data[1] == 1):
        return 1
    elif (data[0] == 0 and data[1] == 1) or (data[0] == 1 and data[1] == 2) or (data[0] == 2 and data[1] == 0):
        return 2
    return None