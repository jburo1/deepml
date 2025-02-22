import numpy as np
def phi_corr(x: list[int], y: list[int]) -> float:
    x,y = np.array(x),np.array(y)
    a=np.sum(((x==1) & (y==1)))
    b=np.sum(((x==0) & (y==1)))
    c=np.sum(((x==1) & (y==0)))
    d=np.sum(((x==0) & (y==0)))
    val=(d*a)-(b*c)/np.sqrt((d+b)*(a+c)*(d+c)*(b+a))
    return round(val,4)

print((phi_corr([1, 1, 0, 0], [0, 0, 1, 1])))