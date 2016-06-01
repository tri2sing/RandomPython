'''
Created on May 31, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict

class MST(object):

    def __init__(self, start_node, num_nodes = 0, num_edges = 0, edges = []):
        self.num_nodes = num_nodes
        self.num_edges = num_edges
        self.start_node = start_node # The start node for MST

        # Adjacency list representation of graph.
        self.graph = defaultdict(list)
        # u, v: vertices, w: weight
        for u, v, w in edges:
            # undirected graph so append edge to each vertex
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

        # Initially none of the vertices are in the MST
        self.in_mst = [False for _ in range(self.num_nodes)]
        
        # Initial distance of all nodes from MST
        self.distance = [float("inf") for _ in range(self.num_nodes)]
        self.distance[self.start_node] = 0
        
        # Initially the parent of a node in MST is unknown
        self.parent = [None for _ in range(num_nodes)]
        
    def _nearest_vertex(self):
        candidate_vertex = None
        candidate_distance = float("inf")
        for i in range(self.num_nodes):
            if self.in_mst[i]:
                # Cannot use a vertex is already in MST
                continue
            if self.distance[i] < candidate_distance:
                candidate_vertex = i
                candidate_distance = self.distance[i]
        return candidate_vertex, candidate_distance
            
    def calculate_mst_weight(self):
        mst_weight = 0
        # While all the vertices are not in the MST
        while sum(self.in_mst) != self.num_nodes:
            vertex, distance = self._nearest_vertex()
            self.in_mst[vertex] = True # Add to MST
            mst_weight += distance
            # For each neighbor of candidate vertex, 
            # adjust the distance from the MST
            for neighbor, weight in self.graph[vertex]:
                if weight < self.distance[neighbor]:
                    self.distance[neighbor] = weight
                    self.parent[neighbor] = vertex
        return mst_weight

        
if __name__ == '__main__':
    # Input node ids are [1, N], I change them to [0, N - 1]
    # num_nodes = number of nodes
    # num_edges = number of edges
    num_nodes, num_edges = map(int, raw_input().strip().split(' '))
    edges = []
    for _ in range(num_edges):
        # u, v = vertices of the edge, w = weight
        u, v, w = map(int, raw_input().strip().split(' '))
        edges.append((u - 1, v - 1, w)) 
    start_node = int(raw_input().strip())
    mst = MST(start_node - 1, num_nodes, num_edges, edges)
    print mst.calculate_mst_weight()
    
    
    