import numpy as np

def dice_score(y_true, y_pred):
    if len(y_true) == 0 and len(y_pred) == 0: return 0.0
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    tp=np.sum(((y_true==1) & (y_pred==1)))
    fp=np.sum(((y_true==0) & (y_pred==1)))
    fn=np.sum(((y_true==1) & (y_pred==0)))
    p=tp/(tp+fp)
    r=tp/(tp+fn)
    if p*r==0: return 0.0
    return round(2*(p*r)/(p+r), 3)

y_true = np.array([1, 1, 0, 1, 0, 1])
y_pred = np.array([1, 1, 0, 0, 0, 1])
print(dice_score(y_true, y_pred))