import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    pe = np.zeros((seq_len,d_model))

    pos = np.arange(seq_len)[:,np.newaxis]

    limit = d_model//2
    indices = np.arange(limit)

    denom = np.exp(-2 *indices *np.log(base) * 1 / d_model)

    result = pos * denom

    pe[:,0:2*limit:2] = np.sin(result)
    pe[:,1:2*limit:2] = np.cos(result)

    if d_model % 2 == 1:
        denom_odd = np.exp(-2 * limit * np.log(base) * 1 / d_model)
        pe[:,-1] = np.sin(pos.ravel()*denom_odd)
    return pe
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    pe = np.zeros((seq_len, d_model))
    
    # Vecteur des positions (lignes) : (seq_len, 1)
    pos = np.arange(seq_len)[:, np.newaxis]
    
    # Vecteur des indices i pour les paires (colonnes) : (d_model // 2,)
    i = np.arange(d_model // 2)
    
    # Calcul du diviseur (fréquences)
    div_term = np.exp(i * -(np.log(base) * 2 / d_model))
    
    # Calcul des angles et remplissage alterné
    angles = pos * div_term
    limit = d_model // 2
    pe[:, 0:2*limit:2] = np.sin(angles)
    pe[:, 1:2*limit:2] = np.cos(angles)
    
    # Gestion du cas d_model impair (dernière colonne)
    if d_model % 2 == 1:
        last_i = d_model // 2
        last_div = np.exp(last_i * -(np.log(base) * 2 / d_model))
        pe[:, -1] = np.sin(pos.ravel() * last_div)
        
    return pe
    '''