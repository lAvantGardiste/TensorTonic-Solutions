import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    if not seqs:
        return np.empty((0, max_len or 0))
    
    if max_len is None:
        max_len = max(len(s) for s in seqs)
    
    N = len(seqs)
    result = np.full((N, max_len), pad_value)
    
    for i, s in enumerate(seqs):
        curr_len = min(len(s), max_len)
        result[i, :curr_len] = s[:curr_len]
        
    return result