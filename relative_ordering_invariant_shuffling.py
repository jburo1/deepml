import numpy as np
def shuffle_data(X, y, seed=None):
    np.random.seed(seed)
    indices = np.random.permutation(len(y))  
    return X[indices], y[indices]
'''
def shuffle_data(X, y, seed=42):
    np.random.seed(seed)
    # perform fisher yates shuffle, generating one set of new indicies across both arrays
    for i in range (len(y)-1,0,-1):
        j = np.random.randint(0,i+1)
        y[i],y[j]=y[j].copy(),y[i].copy()
        X[i],X[j]=X[j].copy(),X[i].copy()
    return X,y
'''    
print(shuffle_data(X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]]),
    y = np.array([1, 2, 3, 4])))