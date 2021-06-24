### load data from provided tsp files and transform it to a a matrix

import os
import numpy as np

def getDist(file):        ## absolute path
    dist = None
    with open(file) as f:
        r=f.readline()
        n = int(r[11:r.index(';')]) # get the matrix size
        dist = np.zeros((n, n), dtype=np.double)
        f.readline()  
        for line in f:
            i, j, c_ij = line.strip(';\n').split()
            i, j = int(i), int(j)
            dist[i, j] = dist[j, i] = float(c_ij)
    return dist