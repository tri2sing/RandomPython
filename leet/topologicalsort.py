'''
Created on Apr 20, 2016

@author: Sameer Adhikari
'''

from collections import defaultdict, deque
class Solution(object):
    
    def __init__(self):
        # Data structure to build the graph
        self.graph = defaultdict(list)
        self.toposort = deque() 
        self.num_vertices = 0
        self.none_mark = -1 # vertex does not have a mark
        self.temp_mark = -2 # vertex has a temporary mark
        self.perm_mark = -3 # vertex has a permanent mark
    
    def buildGraph(self, num_vertices, edges):
        """
        :type prerequisites: List[List[int]]
        :rtype: None
        """
        # Build graph from the input assuming 
        # that the vertex ids are [0, num_vertices-1]
        self.num_vertices = num_vertices
        self.visited = [self.none_mark for _ in range(num_vertices)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            self.graph[u].append(v)

    def visitNeighbors(self, node):
        """
        :type node: int
        :rtype: bool:
        """
        if self.visited[node] == self.temp_mark:
            # Detected a cycle
            return False
        if self.visited[node] == self.none_mark:
            self.visited[node] = self.temp_mark
            # Got to destination of each edge
            for v in self.graph[node]:
                result = self.visitNeighbors(v)
                if not result:
                    return False
            self.visited[node] = self.perm_mark
            self.toposort.appendleft(node)
        return True
            
        
        
    def canFinish(self, num_vertices, edges):
        """
        :type num_vertices: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.buildGraph(num_vertices, edges)
        for i in range(num_vertices):
            if self.visited[i] == self.none_mark:
                possible = self.visitNeighbors(i)
                if not possible:
                    return False
        return True
            
        
if __name__ == '__main__':
    num_vertexes = 2
    edges = [[0, 1], [1, 0]]
    s = Solution()
    print s.canFinish(num_vertexes, edges)
    