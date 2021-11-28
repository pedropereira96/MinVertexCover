# MinVertexCover
Find a minimum vertex cover for a given undirected graph G(V, E), with n vertices and m edges. A vertex cover of G is a set C of vertices, such that each edge of G is incident to, at least, one vertex in C. A minimum vertex cover is a vertex cover of smallest possible size


## Usage
````
usage: main.py [-h] --mode increase/same [--min MIN] [--max MAX] [--vertexs VERTEXS] [--repeat REPEAT]

optional arguments:
  -h, --help            show this help message and exit
  --mode increase/same  Set the mode of vertexs
  --min MIN             Set the min vertex to increase mode
  --max MAX             Set the max vertex to increase mode
  --vertexs VERTEXS     Set the vertexs numbers to same mode
  --repeat REPEAT       Set the numbers of graphs to same mode
  `````

There are 2 execution modes

### Same mode:  
The --vertex and --repeat arguments are required.
In this mode you will need to choose:

--vertexs that correspond to the number of vertex that the graphs will be generated

--repeat that correspond to the number of graphs that will be generated
          
  In this mode, it will be possible to generate several graphs with the same number of vertices and it will be possible to analyze which model used will be more optimal for the problem (smallest number of solutions)
  
### Increase mode:  
The --min and --max arguments are required.
In this mode you will need to choose:

--min that correspond to the number of vertices of the minor graph

--max that corresponds to the number of vertices of the largest graph
          
  In this mode, it will be possible to generate several graphs with the several number of vertices and it will be possible to analyze which model used will be more optimal for the problem with different size graphs (smallest number of solutions)
         
     
