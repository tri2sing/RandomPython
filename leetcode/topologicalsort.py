'''
Created on Apr 20, 2016

@author: Sameer Adhikari
'''

# This works for leetcode problems Course Schedule I & II.

from collections import defaultdict

class Solution(object):
    
    def __init__(self):
        # Data structure to build the graph
        self.unvisited = -1 # vertex does not have a mark
        self.visiting = -2 # vertex has a temporary mark
        self.visited = -3 # vertex has a permanent mark
    
    def buildGraph(self, num_vertices, edges):
        """
        :type prerequisites: List[List[int]]
        :rtype: None
        """
        # Build graph from the input assuming 
        # that the vertex ids are [0, num_vertices-1]
        self.graph = defaultdict(list)
        self.toposort = [] # a deque would be better, but leetcode ...
        self.num_vertices = num_vertices
        self.visited = [self.unvisited for _ in range(num_vertices)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            self.graph[u].append(v)

    def visitNeighbors(self, node):
        """
        :type node: int
        :rtype: bool:
        """
        if self.visited[node] == self.visiting:
            # Detected a cycle
            return False
        if self.visited[node] == self.unvisited:
            self.visited[node] = self.visiting
            # Got to destination of each edge
            for v in self.graph[node]:
                result = self.visitNeighbors(v)
                if not result:
                    return False
            self.visited[node] = self.visited
            self.toposort.append(node)
        return True
            
        
    def canFinish(self, num_vertices, edges):
        """
        :type num_vertices: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.buildGraph(num_vertices, edges)
        for i in range(num_vertices):
            if self.visited[i] == self.unvisited:
                possible = self.visitNeighbors(i)
                if not possible:
                    return False
        return True
     
    def findOrder(self, num_vertices, edges):
        if self.canFinish(num_vertices, edges):
            return self.toposort
        else:
            return []       
        
if __name__ == '__main__':
    s = Solution()
    num_vertices = 2
    edges = [[0, 1], [1, 0]]
    print s.findOrder(num_vertices, edges)
    num_vertices = 2
    edges = [[1, 0]]
    print s.findOrder(num_vertices, edges)
    num_vertices = 4
    edges = [[1,0],[2,0],[3,1],[3,2]]
    print s.findOrder(num_vertices, edges)
    
    
    
    
    