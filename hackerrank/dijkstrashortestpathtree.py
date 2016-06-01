'''
Created on Mar 7, 2016

@author: Sameer Adhikari
'''

'''
Input Format

The first line contains T, denoting the number of test cases.
First line of each test case has two integers 
    N, denoting the number of nodes in the graph and 
    M, denoting the number of edges in the graph.

The next M lines each consist of two space separated integers x y, 
where x and y denote the two nodes between which the edge exists.

The last line of a test case has an integer S, 
denoting the starting position for finding the distances.

Output Format

For each test case print one line wit N-1 space-separated integers.
Each number denotes the shortest distance of the N-1 nodes from the start node (S).
The order of the output corresponds to the node numbers 1 through N (excluding S).
'''



from heapq import heappop, heappush
from sys import stdin
from collections import defaultdict

class MutablePriorityQueue(object):
    '''
    Priority queue that allows changing the priority of an item.
    '''       
    def __init__(self):
        self.heap = []  # Structure to hold the items in the priority queue.
        self.tracker = {}  # Track if an item is in the priority queue or not.
        self.counter = 0  # Ensures that two items with the same priority pop out in their insertion order.
        self.REMOVED = -99  # Label an item as removed without removing from queue to maintain heap invariant.
        
    def add_item(self, item, priority):
        '''
        Add a new item or modify an existing item by adding it again.
        Adding an item multiple times causes the final add to define its priority.
        '''
        if item in self.tracker:
            self.delete_item(item)
        entry = [priority, self.counter, item]
        self.counter += 1
        self.tracker[item] = entry
        heappush(self.heap, entry)
    
    def delete_item(self, item):
        '''
        Delete an existing item.
        Raise a KeyError if not found.
        '''
        entry = self.tracker.pop(item)
        entry[-1] = self.REMOVED  # Set the id of the item to the label for removed.

    def pop_item(self):
        '''
        Remove and return the lowest priority item.
        Raise a KeyError if not found.
        '''
        while self.heap:
            _, _, item = heappop(self.heap)
            # The item has use only if it is still logically in the queue.
            if item is not self.REMOVED:
                del self.tracker[item]
                return item
        return None
                
    def is_empty(self):
        return not self.tracker            
    
    def print_queue(self):
        for item in self.heap:
            print '[Item = {0} Distance = {1}]'.format(item[2], item[0]),
        print 

class Graph(object):
    '''
    Represent a graph with vertices and edges.
    '''

    def __init__(self, num_nodes):
        '''
        Constructor
        '''
        # using an adjacency vertex representation to store the graph
        self.graph = defaultdict(list)
        self.num_nodes = num_nodes
        
    def add_edge(self, src, des):
        '''
        Add the given edge to the graph.
        This is an undirected graph.
        '''
        self.graph[src].append(des)
        self.graph[des].append(src)
        
    
    def print_graph(self):
        '''
        Print the graph in adjacency vertex form.
        '''
        for key, val in self.graph.iteritems():
            print str(key) + ": " + str(val) 
                  
    def find_min_distance_all(self, start_node, weight):
        '''
        Find the minimum distance from the start current to all the nodes.
        start_node: current to start the paths.
        weight: to use for each edge in the graph.
        '''
        # Set the distance for each current to unreachable to begin with
        # Input data numbers vertices from 1...N, so we pad the list.
        distances = [float("inf") for _ in range(self.num_nodes + 1)]
        # The distance of the start current from itself is 0
        distances[start_node] = 0
        queue = MutablePriorityQueue()
        for i in range(1, self.num_nodes + 1):
            queue.add_item(i, distances[i])

        # Initialize the previous current in the path to this current as None
        previous = [None for _ in range(self.num_nodes + 1)]
        
        print 'Num nodes = {}, Start node = {}'.format(self.num_nodes, start_node)
        
        while not queue.is_empty():
            # Find the node with the minimum distance in the queue
            current = queue.pop_item()
            # For each neighbor of the current
            # If the node does not have neighbors the returned list is empty
            for neighbor in self.graph[current]:
                alternate = distances[current] + weight
                if alternate < distances[neighbor]:
                    distances[neighbor] = alternate
                    previous[neighbor] = current
                    # Update the distance for the item in the queue
                    queue.add_item(neighbor, distances[neighbor])
            print
        # Skip the 0th element padded to the left in return values
        return distances[1:], previous[1:]

if __name__ == '__main__':
    # The default weight for each edge is 6 in this problem
    weight = 6
    num_tests = int(stdin.readline().strip())
    for _ in range(num_tests): 
        line = stdin.readline().strip()
        num_nodes, num_edges = (int(s) for s in line.split())
        graph = Graph(num_nodes)
        for _ in range(num_edges):
            line = stdin.readline().strip()
            src, des = (int(s) for s in line.split())
            graph.add_edge(src, des)
        start_node = int(stdin.readline().strip())
        distances, previous = graph.find_min_distance_all(start_node, weight)
        for distance in distances:
            if distance == 0:
                continue
            elif distance == float('inf'):
                print -1,
            else:
                print distance,
        print ''
                            
            
            
            
            
            
            
            
            
            
            
        
