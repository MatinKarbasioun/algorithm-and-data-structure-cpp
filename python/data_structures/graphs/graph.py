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

"""



class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source_vertex, target):
        self.vertices[source_vertex].append(target)



if __name__ == '__main__':
    g = Graph()
    g.add_vertex('matin')
    g.add_vertex('omid')
    g.add_vertex('hamed')

    g.add_edge('matin', 'omid')
    g.add_edge('matin', 'hamed')
    g.add_edge('omid', 'hamed')

    print(g.vertices)