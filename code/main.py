
from matplotlib.colors import rgb2hex
from graph import Graph
from indexer import Indexer
import sys
import getopt
import random
import time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import pandas as pd


    
def random_graph(vertices_number: int) :
    graph=[]

    # for each couple of nodes, add an edge from u to v
    # if the number randomly generated is greater than probability probability
    for i in range(vertices_number):
        for j in range(i + 1, vertices_number):
            if random.random() < 0.5:
                graph.append((i,j))
    return graph

def process(nvertexs, graph,  approx, vertexs, greedy ):
    
    G = Graph(nvertexs)
    for (u,v) in graph:
        G.addEdge(str(u),str(v))

    G.show_graph(str(nvertexs))

    #write graph on txt file
    G.import_graph_to_txt()
    
    vertexs.append(str(nvertexs))
    print("******************************************************")
    print("Graph with {} vertices".format(nvertexs))
    print()
    G.print_graph(True)
    print()
    
    #Approx Vertex Cover Algorithm
    print("Approx Vertex Cover Algorithm")
    tic = time.time()
    print("Resultado: " + str(G.aprox_algorithm(name=nvertexs)))
    t_approx =time.time() - tic
    approx.append(t_approx)
    print("Tempo de execução: " + str(t_approx))
    print()

    
    #Greedy Algorithm
    print("Greedy Algorithm")
    tic = time.time()
    print("Resultado: " + str(G.greedy_algorithm(name=nvertexs)))
    t_greedy =time.time() - tic
    greedy.append(t_greedy)
    print("Tempo de execução: " + str(t_greedy))
    print()
    
    
    return approx, vertexs, greedy

       
def create_times_graph(points, approx ,greedy):
    # x-coordinates of left sides of bars
    bar_width = 0.3
    r1 = np.arange(len(approx))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    left = points
    
    # heights of bars
    height = nvertexs
    
    # labels for bars
    tick_label = nvertexs
    
    plt.figure(figsize=(10,5))

    # plotting a bar chart
    plt.bar(r1, approx,  width = bar_width, color = '#6A5ACD', tick_label="Approx Min Vertex Cover")
    plt.bar(r2, greedy,  width = bar_width, color = '#6495ED', tick_label="Greedy Algorithm")
    # naming the x-axis
    plt.xlabel('n Vertexs')
    plt.xticks([r + bar_width for r in range(len(points))],[str(r) + " vertexs" for r in range(len(points))])
    # naming the y-axis
    plt.ylabel('Times')
    # plot title
    plt.title("Min Vertex Cover")
    
    # function to show the plot
    plt.legend(('Approx Min Vertex Cover','Greedy Algorithm'))
    plt.show()
    plt.close()


if __name__ == "__main__":
    random.seed(106346) 

    approx = []
    vertexs = []
    greedy = []
    greedy_p = []

    #Create x graphs with x vertexs
    for nvertexs in range(2,10):

        #generate random graph
        graph = random_graph(nvertexs)
        while graph == []:
            graph = random_graph(nvertexs)


        approx, vertexs, greedy = process(nvertexs , graph, approx, vertexs, greedy )

    print(approx)
    print(greedy_p)
    print(greedy)
    print(vertexs)

    create_times_graph(vertexs, approx, greedy)

