'''
    Write a class to represent a Graph with methods to add vertices and edges, and perform BFS and DFS traversals.
'''

from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_vertex(self,vertex):
        '''Add a vertex to the graph'''
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        '''Add an edge between two vertices'''
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def bfs(self, start_vertex):
        '''Breadth-First Search traversal'''
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start_vertex):
        '''Depth-First Search traversal'''
        visited = set()
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

# Example Usage
g = Graph()
g.add_vertex(0)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,4)

print("BFS traversal: ")
g.bfs(0) # OUTPUT: 0 1 2 3 4 

print("\nDFS traversal: ")
g.dfs(0)  # OUTPUT: 0 1 3 2 4 