import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    if seqs is None:
        return np.array(0,0)

    if max_len is None:
        max_len = max(len(s) for s in seqs)

    a = np.full((len(seqs),max_len),pad_value)
    
    for i , s in enumerate(seqs):
        f = min(max_len or 0, len(s))
        a[i,:f] = s[:f]

    return a
        