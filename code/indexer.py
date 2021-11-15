class Indexer:
 
    def __init__(self):
        self.path_file = '../content/output.txt'

    def create_file(self):
        file = open(self.path_file, "w")  
        file.write("id: {(x, y): n_edges}\n")
        file.close()

    def write_file(self, graph):
        file = open(self.path_file, "a")  
        file.write(str(graph)+ "\n")
        file.close() 