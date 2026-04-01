import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if seqs is None:
        return np.empty((0, max_len or 0))
    
    if max_len is None:
        max_len = max(len(s) for s in seqs)

    N = len(seqs)
    result = np.full((N,max_len),pad_value)

    for i,s in enumerate(seqs):
        f = min(max_len,len(s))
        result[i,:f] = s[:f]
    
    return result
    