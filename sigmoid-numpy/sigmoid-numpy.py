import numpy as np

def sigmoid(x):
    y = np.asanyarray(x,dtype=float)
    
    denom = 1 + np.exp(-y)
    return 1/denom
