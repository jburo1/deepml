import numpy as np

def f_score(y_true, y_pred, beta):
    tp=np.sum(((y_true==1) & (y_pred==1)))
    fp=np.sum(((y_true==0) & (y_pred==1)))
    fn=np.sum(((y_true==1) & (y_pred==0)))
    p=tp/(tp+fp)
    r=tp/(tp+fn)
    return np.round(((1+beta**2)*(p*r))/((beta**2 * p) + r),3)
    
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
beta = 1
print(f_score(y_true, y_pred, beta))

y_true = np.array([1, 0, 1, 1, 0, 0]) 
y_pred = np.array([1, 0, 0, 0, 0, 1]) 
beta = 1 
print(f_score(y_true, y_pred, beta))


