from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
import sys
import getopt
import random
import time

def usage():
    print("Usage: python3 main.py ")

if __name__ == "__main__":
    num_vertices = 6
    G=nx.Graph()
    G.add_nodes_from([x for x in range(0, num_vertices)])

    tic = time.time()
    #graph = Graph(num_vertices)
    for i in range(0,num_vertices):
        n_iters = random.choice([x for x in range(1,num_vertices)])
        used_vertices = []
        for iteration in range(1, n_iters):
            j = list( set([ x for x in range(num_vertices) if x != i]) - set(used_vertices))
            j = random.choice(j)
            #print("Creating edge: G[%d][%d]" %  (i,j))
            #graph.add_edge(i,j)
            G.add_edge(i,j)
            used_vertices.append(j)
    toc = time.time()
    print("Created Graph with %d nodes and %d edges in %.3f ms" % (num_vertices, len(G.edges), 1000*(toc-tic)))
    #result = graph.color_matrix()
    # Available functions for visualizing matrixes 


    nx.draw(G, with_labels=True)
    plt.savefig("../generated_graph.png") # save as png
    #plt.show() # display
    sys.exit()