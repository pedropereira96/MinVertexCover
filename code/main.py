
from graph import Graph
from indexer import Indexer
import sys
import getopt
import random
import time


def usage():
    print("Usage: python3 main.py ")

if __name__ == "__main__":
    random.seed(106346)
    """g = Graph(8)
    g.addEdge('1', '2')
    g.addEdge('1', '4')
    g.addEdge('2', '5')
    g.addEdge('2', '3')
    g.addEdge('5', '6')
    g.addEdge('3', '6')
    g.addEdge('3', '7')
    g.addEdge('3', '8')"""


    """g = Graph(8)
    g.addEdge('1', '2')
    g.addEdge('1', '4')
    g.addEdge('2', '5')
    g.addEdge('2', '3')
    g.addEdge('5', '6')
    g.addEdge('3', '6')
    g.addEdge('3', '7')
    g.addEdge('3', '8')
    print(g.greedy_min_vertex_cover())"""
    for nvertexs in range(1,10):
        print("/////////////GRAPH N {} ///////////////////".format(nvertexs))
        g = Graph(nvertexs)
        
        #Escolher vértice e verificações se já existem
        for v in range(0,nvertexs): 
            
            x = str(random.randrange(1,9))
            y = str(random.randrange(1,9))

            while (((x,y) in g.print_graph(False)) or ((y,x) in g.print_graph(False))) or x==y :
                x = str(random.randrange(1,9))
                y = str(random.randrange(1,9))

            
            g.addEdge( x , y )
        
        g.print_graph(True)    
        g.show_graph(name=nvertexs)

        #escreve o grafico no ficheiro txt
        g.import_graph_to_txt()

        #print(g.greedy_min_vertex_cover())
        print()
        print("Approx Vertex Cover Algorithm")
        tic = time.time()
        print("Resultado: " + str(g.aprox_algorithm(name=nvertexs)))
        print("Tempo de excução: " + str(time.time() - tic))
        print()
        print("Greedy Algorithm PROF")
        tic = time.time()
        print("Resultado: " + str(g.greedy_min_vertex_cover()))
        print("Resultado: " + str(g.greedy_min_vertex_cover()))
        print("Resultado: " + str(g.greedy_min_vertex_cover()))
        print("Tempo de excução: " + str(time.time() - tic))
        print()
        
        print("Greedy Algorithm")
        tic = time.time()
        print("Resultado: " + str(g.greedy_algorithm(name=nvertexs)))
        print("Resultado: " + str(g.greedy_algorithm(name=nvertexs)))
        print("Resultado: " + str(g.greedy_algorithm(name=nvertexs)))
        print("Tempo de excução: " + str(time.time() - tic))
        print()
        print()
    #i = Indexer()
    #i.create_file()
    #i.write_file(g.print_graph())
    #g.printVertexCover()
