from graph import Graph
import sys
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
import pylab
from argparse import ArgumentParser


class Main:

    def __init__(self):
        self.greedy_results = {}
        self.approx_results = {}

        self.greedy_times = []
        self.approx_times = []

        self.approx_counts = []
        self.greedy_counts = []



def random_graph(vertices_number: int) :
    graph=[]

    # for each couple of nodes, add an edge from u to v
    # if the number randomly generated is greater than probability probability
    for i in range(vertices_number):
        for j in range(i + 1, vertices_number):
            if random.random() < 0.5:
                graph.append((i,j))
    return graph

def process(m, nvertexs, graph,  approx, vertexs, greedy,  clean, extra_name="" ):
    
    G = Graph(nvertexs)
    for (u,v) in graph:
        G.addEdge(str(u),str(v))

    #create de png image
    G.show_graph(str(nvertexs)+str(extra_name))

    #write graph on txt file
    G.import_graph_to_txt(clean)
    
    #for x axis 
    vertexs.append(str(nvertexs)+str(extra_name))

    print("\n******************************************************")
    print("Graph with {} vertices \n".format(str(nvertexs)+str(extra_name)))

    print("Edges:")
    G.print_graph(True)
    print()


    #Greedy Algorithm
    print("Greedy Algorithm:")
    tic = time.time() #Iniciar tempo
    greedy = G.greedy_algorithm(nvertexs) #Excutar 
    time_value = time.time() - tic
    m.greedy_times.append(time_value) #Adicionar tempo
    m.greedy_results[str(nvertexs) + str(extra_name)] = greedy #adicionar resultado à class main
    m.greedy_counts.append(len(greedy))
    print(greedy)
    print("Execution Time: " + str(time_value))

    print("")

    #Aprox Algorithm
    print("Aprox Algorithm:")
    tic = time.time() #Iniciar tempo
    aprox = G.aprox_algorithm(nvertexs) #Excutar 
    time_value = time.time() - tic 
    m.approx_times.append(time_value)#Adicionar tempo
    m.approx_results[str(nvertexs) + str(extra_name)] = aprox #adicionar resultado à class main
    m.approx_counts.append(len(aprox))
    print(aprox)
    print("Execution Time: " + str(time_value))


    print("")

def create_times_graph(m, min, max):
    # x-coordinates of left sides of bars
    bar_width = 0.3
    r1 = [ x for x in range(min, max)]
    r2 = [x + bar_width for x in r1]

    
    plt.figure(figsize=(15,7))

    # plotting a bar chart
    plt.bar(r1, m.approx_times,  width = bar_width, color = '#054A91', tick_label="Approx Min Vertex Cover")
    plt.bar(r2, m.greedy_times,  width = bar_width, color = '#3E7CB1', tick_label="Greedy Algorithm")

    # naming the x-axis
    plt.xlabel('n Vertexs')
    plt.xticks([r + bar_width for r in range(min, max)],[str(r) for r in range(min, max)])
    # naming the y-axis
    plt.ylabel('Times')
    # plot title
    plt.title("Min Vertex Cover - Times")
    
    # function to show the plot
    plt.legend(('Approx Min Vertex Cover','Greedy Algorithm'))
    plt.savefig("content/times_graphics.png")
    #plt.show()
    plt.close()

def create_solutions_graph(m, min, max):
    # x-coordinates of left sides of bars
    bar_width = 0.3
    r1 = [ x for x in range(min, max)]
    r2 = [x + bar_width for x in r1]
    
    
    plt.figure(figsize=(15,7))

    # plotting a bar chart
    plt.bar(r1, m.approx_counts,  width = bar_width, color = '#054A91', tick_label="Approx Min Vertex Cover")
    plt.bar(r2, m.greedy_counts,  width = bar_width, color = '#3E7CB1', tick_label="Greedy Algorithm")
    # naming the x-axis
    plt.xlabel('n Vertexs')
    plt.xticks([r + bar_width for r in range(min, max)],[str(r) for r in range(min, max)])
    # naming the y-axis
    plt.ylabel('Solutions')
    # plot title
    plt.title("Min Vertex Cover - Solutions")
    
    # function to show the plot
    plt.legend(('Approx Min Vertex Cover','Greedy Algorithm'))
    plt.savefig("content/solutions_graphics.png")
    #plt.show()
    plt.close()

def create_solutions_graph_same_mode(m, repeat, vertexs):
    # x-coordinates of left sides of bars
    bar_width = 0.3

    r1 = [ x for x in range(repeat)]
    r2 = [x + bar_width for x in r1]
    
    plt.figure(figsize=(15,7))

    # plotting a bar chart
    plt.bar(r1, m.approx_counts,  width = bar_width, color = '#054A91', tick_label="Approx Min Vertex Cover")
    plt.bar(r2, m.greedy_counts,  width = bar_width, color = '#3E7CB1', tick_label="Greedy Algorithm")
    # naming the x-axis
    plt.xlabel('Graph')
    plt.xticks([r + bar_width for r in range(repeat)],[str(r) for r in range(repeat)])
    # naming the y-axis
    plt.ylabel('Solutions')
    # plot title
    plt.title("Min Vertex Cover - Solutions - {} Vertexs".format(vertexs))
    
    # function to show the plot
    plt.legend(('Approx Min Vertex Cover','Greedy Algorithm'))
    plt.savefig("content/solutions_graphics.png")
    #plt.show()
    plt.close()

def write_solutions(file_path, values):
    """write solutions on txt file"""
    with open(file_path, "w") as output_file:
        for row in values.keys():
            print(str(row) + " : " + str(values[row]), file=output_file)

def same(nvertexs, ngraphs):
    """Same Mode """
    approx = []
    vertexs = []
    greedy = []
    clean = True
    m = Main()
    #Create x graphs with x vertexs
    for n in range(ngraphs):
        #generate random graph
        graph = random_graph(nvertexs)
        extra_name = "."+str(n)
        while graph == []:
            graph = random_graph(nvertexs)
        process(m, nvertexs , graph, approx, vertexs, greedy, extra_name=extra_name, clean=clean)
        clean=False
    
    print("\n")

    print("All final results:")
    print("\tGreedy Algorithm")
    for i in m.greedy_results:
        print("\t" + str(i) + " : " + str(m.greedy_results[i]))
    print("")
    print("\tAprox Algorithm")
    for i in m.approx_results:
        print("\t" + str(i) + " : " + str(m.approx_results[i]))
    print("")


    write_solutions("content/greedy_solutions.txt", m.greedy_results)
    write_solutions("content/aprox_solutions.txt", m.approx_results)
  

    create_solutions_graph_same_mode(m, repeat=ngraphs, vertexs=nvertexs)

def increase(min, max):
    """Increase mode"""

    approx = []
    vertexs = []
    greedy = []

    min_vertexs = min
    max_vertexs = max
    m = Main()
    clean = True
    #Create x graphs with x vertexs
    for nvertexs in range(min_vertexs, max_vertexs):
        #generate random graph
        graph = random_graph(nvertexs)
        while graph == []:
            graph = random_graph(nvertexs)
        process(m, nvertexs , graph, approx, vertexs, greedy, clean=clean)
        clean = False
    
    print("\n")

    
    print("All final results:")
    print("\tGreedy Algorithm")
    for i in m.greedy_results:
        print("\t" + str(i) + " : " + str(m.greedy_results[i]))
    print("")
    print("\tAprox Algorithm")
    for i in m.approx_results:
        print("\t" + str(i) + " : " + str(m.approx_results[i]))
    print("")
    

    write_solutions("content/greedy_solutions.txt", m.greedy_results)
    write_solutions("content/aprox_solutions.txt", m.approx_results)


    create_times_graph(m, min_vertexs, max_vertexs)
    create_solutions_graph(m, min_vertexs, max_vertexs)

if __name__ == "__main__":
    random.seed(106346) 

    parser = ArgumentParser()
    # (increase - increases the number of vertices from minimum to maximum) (same - generate several graphs with same vertexs numbers)
    parser.add_argument("--mode", help="Set the mode of vertexs ", required=True, 
                        type=str, metavar="increase/same")
    parser.add_argument("--min", help="Set the min vertex to increase mode",
                        type=int)
    parser.add_argument("--max", help="Set the max vertex to increase mode", 
                        type=int)
    parser.add_argument("--vertexs", help="Set the vertexs numbers to same mode", 
                        type=int)
    parser.add_argument("--repeat", help="Set the numbers of graphs to same mode",
                        type=int)

    args = parser.parse_args()

    same_mode = False
    increase_mode = False

    if args.mode == 'same':
        same_mode = True
        if not args.vertexs or not args.repeat:
            print("To set same mode, --vertexs and --repeat is required")
            print(parser.parse_args(['-h']))
            sys.exit()
        nvertexs = args.vertexs
        ngraphs = args.repeat

        same(nvertexs, ngraphs)

    if args.mode == 'increase':
        same_mode = True
        if not args.min or not args.max:
            print("To set increase mode, --min and --max is required")
            print(parser.parse_args(['-h']))
            sys.exit()
        min = args.min
        max = args.max   

        increase(min, max) 
