from random import choice

# If the code is not Cython-compiled, we need to add some imports.
from cython import compiled

if not compiled:
    from mazelib.solve.MazeSolveAlgo import MazeSolveAlgo
import heapq as hq
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
        self.unvisited_cells = set()
    def _solve(self):
        current = self.start
        solution = []
        solution.append(current)
        tdists = {}
        tdists[current] = 0
        self.visited_cells.add(current)









        return solution