
from collections import Counter
import numpy as np

def confusion_matrix(data):
    data = np.asarray(data)
    y_true, y_pred = data[:,0],data[:,1]
    tp=np.sum(((y_true==1) & (y_pred==1)))
    tn=np.sum(((y_true==0) & (y_pred==0)))
    fp=np.sum(((y_true==0) & (y_pred==1)))
    fn=np.sum(((y_true==1) & (y_pred==0)))
    return ([[tp, fn],[fp, tn]])
    
data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]
print(confusion_matrix(data))
