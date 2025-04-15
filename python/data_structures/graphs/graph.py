"""

graphs can have cycles

real-world use cases
(store)
1- friendship
2- follows
3- likes
4- etc


Locations and distances
- optimize routes

Graph databases

Searching and sorting algorithms

Robotic arms
- represented as a graph based on their joint and their arms
- find the best reconfiguration of their arms


Loops: connect a vertex to itself
Multiple Edges: two vertices can be connected by multiple edges
Density: how many edges you have in terms of the number of vertices

Dense graph:
- in a dense graphs, |E| ~= |V| ** 2
- in a gense graphs, a large fraction of pairs of vertices are connected by edges


Sparse graph:
- in a sparse graphs, |E| ~= |V|
- each vertex has only a few edges

Exploring Graph Applications:
- finding routes
- ensuring connectivity
- solving puzzles and mazes

Path:
- is a sequence of vertices v0, v1, v2, ..., vn so that for all i, (vi, vi+1) is an edge of G

Reachability:
- return collection of vertices v of graph so that there is a path from s to v


Depth-First Ordering:
- we will explore new edges in depth-first order. we will follow a long path forward, only backtracking when we
hit a dead end.

(backtracking)
- when a vertex that we have already seen before
- hit dead-end --> backtrack one step then try going forwards again from that new vertex that we found

"""



class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source_vertex, target):
        self.vertices[source_vertex].append(target)

    def reachability(self, target_vertex) -> list[str]: # vertices list
        pass

    def component(self, node):
        pass

    def explore(self, vertex):
        for (v, w) in self.vertices:
            if not visited(w):
                self.explore(w)





if __name__ == '__main__':
    g = Graph()
    g.add_vertex('matin')
    g.add_vertex('omid')
    g.add_vertex('hamed')

    g.add_edge('matin', 'omid')
    g.add_edge('matin', 'hamed')
    g.add_edge('omid', 'hamed')

    print(g.vertices)