from random import choice

# If the code is not Cython-compiled, we need to add some imports.
from cython import compiled

if not compiled:
    from mazelib.solve.MazeSolveAlgo import MazeSolveAlgo

import heapq
class Dijkstra(MazeSolveAlgo):
    """The Algorithm:
    1. Mark all nodes unvisited and create univisited set
    2. Assign every node a tentative distance value, 0 for current node, infinity for other nodes initially, set initial node as current.
    The tentative distance of a node is the shortest path from current node to the starting node.
    3. For current node calculate the tentative distances of all unvisited neighbors. If the distance of neighboring node through this node is
    greater than calculated, then set it to the calculated distance otherwise keep the current value of the neighbor.
    4. After considering all unvisited neighbors mark the current node visited and remove it from unvisited set. This node wont be checked again
    5. If goal node has been marked visited or if the smallest tentative distance among unvisited nodes is infinity (if theres no path), then stop 
    6. Otherwise select the smallest distance unvisited node and set it as current and go to step 3.   
    """

    def __init__(self):
       self.solution = []
       self.visited = set()
       self.pq = []
       self.distances = {}

    def _solve(self):
        if self._on_edge(self.start):
            current = self._push_edge(self.start)
            self.solution.append(current)
        self.visited.add(current)
        self.pq.append((0,current))
        # Pick nodes to travel to based on Dijkstra's algorithm
        while not self._within_one(self.solution[-1], self.end):
            distNode = heapq.heappop(self.pq)
            current_distance = distNode[0]
            current = distNode[1]
            self.distances[current] = current_distance
            nxt = self.what_next(self._find_unblocked_neighbors(self.solution[-1]))
            self.solution.append(self._midpoint(self.solution[-1], nxt))
            self.solution.append(nxt)
        return [self.solution]
    # Find what node to visit next using Dijkstra algorithm step 3
    def what_next(self, ns,):
        for neighbor in ns:
            t_distance = self.distances[self.solution[-1]] + 1
            if neighbor not in self.visited or t_distance < self.distances[neighbor]:
                self.distances[neighbor] = t_distance
                heapq.heappush(self.pq, (t_distance, neighbor))
        node = heapq.heappop(self.pq)[1]
        self.visited.add(node)
        return node

           






