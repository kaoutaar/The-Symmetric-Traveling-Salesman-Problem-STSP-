
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from distMat import getDist
from pathlib import Path

def christof(data):
 # graph G        
    dist=getDist(data)  # load distance (cost) matrix
    
    n=len(dist)
    v=range(n)
    G=nx.Graph()
    G.add_nodes_from(v)
    for i in v:
        for j in range(i+1,n):
            G.add_edge(i,j,weight=dist[i,j])
            G.add_edge(j,i,weight=dist[i,j]) # symmetry
    
    '''    
    nx.draw(G, with_labels=True, arrows=True)
    plt.draw()
    plt.show()
    plt.savefig('a')'''
    
 # 1) find MST
    mst = nx.minimum_spanning_tree(G)
    

    '''
    nx.draw(mst, with_labels=True, arrows=True)
    plt.draw()
    plt.show()
    plt.savefig('b')'''
    
 # 2) Extract odd degree vertices
    S = {v for v, d in mst.degree() if d%2 == 1}
    g = G.subgraph(S)
    
    '''
    nx.draw(g, with_labels=True, arrows=True)
    plt.draw()
    plt.show()
    plt.savefig('c')  '''  
    
    
 # 3) find Min weight perfect matching in g 
    max_weight = max((e[-1]['weight'] for e in g.edges(data=True)))+1
    for e in g.edges(data=True):
        e[-1]['weight'] = max_weight - e[-1]['weight']
    M = nx.max_weight_matching(g) 
    
    '''
    k=nx.Graph()
    k.add_edges_from(list(M))
    nx.draw(k, with_labels=True)
    plt.draw()
    plt.show()
    plt.savefig('d') '''
    
    
 # 4) construct eulerian tour
    assert nx.is_perfect_matching(g, M)
    mst = nx.MultiGraph(mst)
    for e in M:
        mst.add_edge(*e)
    E = list(nx.eulerian_circuit(mst))  
    
    
    '''
    y=nx.Graph()    
    y.add_edges_from(E)
    nx.draw(y, with_labels=True, arrows=True)
    plt.draw()
    plt.show()
    plt.savefig('e') '''
    
    
 # 5) extract hamiltonian tour
    visited_nodes = {E[0][0]}
    adjacency = np.zeros((n, n), dtype=np.int)
    i = 0
    start = E[0][0]
    while i < len(E):
        while i < len(E)-1 and E[i][1] in visited_nodes:
            i += 1
        adjacency[start,E[i][1]] = 1
        visited_nodes.add(E[i][1])
        start = E[i][1]
        i += 1
    obj = (adjacency*dist).sum()
    return adjacency, obj

    '''
    o = nx.from_numpy_matrix(adjacency*dist) 
    nx.draw(o, with_labels=True)
    plt.draw()
    plt.show()
    plt.savefig('w') '''