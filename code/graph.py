from collections import defaultdict
from collections import OrderedDict
import networkx as nx
import matplotlib.pyplot as plt
import sys
import getopt
import random 
import time
import pylab
import pandas as pd
import json
import heapq
 
class Graph:
 
    def __init__(self, vertices):
         
        self.V = vertices
        self.graph = []

        self.graph_file = "content/graph.txt"
        self.greedy_file = "content/greedy_algorithm/process_graph_{}.csv"
        self.aprox_file = "content/aprox_algorithm/process_graph_{}.csv"

    def addEdge(self, u, v):
        edge = (u,v)
        self.graph.append(edge)

    def import_graph_to_txt(self):
        #clean file
        clean = open(self.graph_file, "w")  
        clean.truncate()
        clean.close()

        #Wite graphs
        file = open(self.graph_file, "a")  

        vertex = {}
        for x,y in self.graph:
            #Add all vertexs
            if x not in vertex:
                vertex[x] = []
            if y not in vertex:
                vertex[y] = []

            if x not in vertex[y]:
                vertex[y].append(x)
            if y not in vertex[x]:
                vertex[x].append(y)   
        
            file.write(str(vertex)+ "\n")
        file.close() 
    


    def print_graph(self, print_):
        if print_:
            print(self.graph)
        return self.graph

    def show_graph(self, name:str):

        G = nx.Graph()
        G.add_edges_from(self.graph, weight=1)
        nx.draw(G, with_labels=True)
        plt.savefig("content/graphs/generated_graph_"+str(name)+".png")
        plt.tight_layout()
        #plt.show()
        #pylab.show()
        plt.close()


    def adjacency_table(self):
        #self.graph = array( ( 'A','B' ))
        #adjacency_table = {'A':{ neighbors: ['B','C'] ,  degree:2 },  ...   }
        #criar [(u,v), (v,u)]
        graph_data = self.graph
        graph_data.extend( [(v,u) for u,v in self.graph] )

        adjacency = {}
        for x,y in graph_data:
            if x not in adjacency.keys():
                adjacency[x] = { 'neighbors' : [], 'degree': 0 , 'visited' : False}
            adjacency[x]['neighbors'].append(y)
            adjacency[x]['degree'] += 1
        
        return adjacency   
  

    def show_results(self, adjacency, stage, option, name):
        
        result = {'':[], 'vector':[],'neighbors':[], 'degree':[],'visited':[], 'option': []}
        
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

        result[''].append(str(ordinal(stage)) + " Stage")
        result['vector'].append("")
        result['neighbors'].append("")
        result['degree'].append("")
        result['visited'].append("")
        result['option'].append("")


        #for term in adjacency.keys():
        #    #if not adjacency[term]['visited']:
        #    print("  "+str(count) +"  |  "+str(term) + "  |  " + str(adjacency[term]['neighbors']) + "  |  " + str(adjacency[term]['degree']) + "  |  " +str(adjacency[term]['visited']))
        #    count+=1
        count = 1
        for term in adjacency.keys():
            result[''].append('')
            result['vector'].append(term)
            result['neighbors'].append(adjacency[term]['neighbors'])
            result['degree'].append(adjacency[term]['degree'])
            result['visited'].append(adjacency[term]['visited'])
            result['option'].append("X" if option == term else "")
            count+=1
        
        #Apenas para agar tudo do csv
        if stage == 1:
            f = open(self.greedy_file.format(name), "w+")
            f.close()

        with open(self.greedy_file.format(name), 'a') as f:
            df = pd.DataFrame(data=result)
            df.append(pd.Series(), ignore_index=True)
            if stage == 1:
                df.to_csv(f,header=True, index=False, line_terminator='\n')
            else: 
                df.to_csv(f,header=False, index=False, line_terminator='\n')


        


    def greedy_algorithm(self,name):
        adjacency = self.adjacency_table()
        count=1
        final_result = []
        #apenas corre os que ainda não foram visitados
        while False in tuple((adjacency[key]['visited']) for key in adjacency):
            #Para procurar a melhor opção para o vértice
            #  (Conter mais número de arestas(vértices associados) e que ainda não tenham sido visitados)
            max = -1
            for key in adjacency:
                if adjacency[key]['degree'] > max and adjacency[key]['visited'] == False:
                    term = key
                    max = adjacency[key]['degree']
            #Se o vértice ainda não foi visitado, então vamos visita-lo
            if not adjacency[term]['visited']:
                adjacency[term]['visited'] = True
                final_result.append(term)
                #Iniciar remoção dos termo atual no vértices associados
                to_remove_list = adjacency[term]['neighbors']
                for x in to_remove_list:
                    #remover
                    adjacency[x]['neighbors'].remove(str(term))
                    #atualizar grau
                    adjacency[x]['degree'] = len(adjacency[x]['neighbors'])
                    #caso fique sem vetores associados, coloco como visitado para não voltar a verificar
                    if len(adjacency[x]['neighbors']) == 0:
                        adjacency[x]['visited'] = True
            count += 1
        return final_result
   


    def create_dictionary(self):
        matrix={}
        z=0
        for value in self.graph:
            matrix['A'+str(z)] = value
            z+=1
        return matrix

    def aprox_algorithm(self, name):

        #Aprox vertex cover algorithm
        # C←∅
        #while E != ∅
        #    pick any {u, v} ∈ E
        #    C ← C ∪ {u, v}
        #    delete all eges incident to either u or v
        #return C
        

        E = self.create_dictionary()
        
        C = []
        #Enquanto a matriz conter dados
        while E:
            arbitrary = random.choice(list(E.keys()))
            u, v = tuple(E[str(arbitrary)])
            aux=[]
            C.append(E[arbitrary][0])
            C.append(E[arbitrary][1])
            aux.extend(E)
            for q in aux:
                x,y = tuple(E[q])
                if x == u or x== v or y==u or y==v:
                    E.pop(q)  
        return C

            
            
    def adjacency_table1(self):

        graph_data = self.graph
        graph_data.extend( [(v,u) for u,v in self.graph] )

        adjacency = {}
        for x,y in graph_data:
            if x not in adjacency.keys():
                adjacency[x] = []
            adjacency[x].append(y)
        
        return adjacency   
        

    def greedy_min_vertex_cover(self):
        graph = self.adjacency_table1()
        queue: list[list] = []
        for key, value in graph.items():
            # O(log(n))
            heapq.heappush(queue, [len(value), (key, value)])
        # chosen_vertices = set of chosen vertices
        chosen_vertices = set()
        # while queue isn't empty and there are still edges
        #   (queue[0][0] is the rank of the node with max rank)
        while queue and queue[0][0] != 0:
            # extract vertex with max rank from queue and add it to chosen_vertices
            argmax = heapq.heappop(queue)[1][0]
            chosen_vertices.add(argmax)
            # Remove all arcs adjacent to argmax
            for elem in queue:  
                # if v haven't adjacent node, skip
                if elem[0] == 0:
                    continue
                # if argmax is reachable from elem
                # remove argmax from elem's adjacent list and update his rank        
                if argmax in elem[1][1]:
                    index = elem[1][1].index(argmax)
                    del elem[1][1][index]
                    elem[0] -= 1     
            # re-order the queue
            heapq.heapify(queue)      
        return chosen_vertices


