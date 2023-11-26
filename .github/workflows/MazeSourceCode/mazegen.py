# Group 21, Maze Solving AI Source Code
# Connor Thompson, John Huddleston, Aidan Blashe
from display import showPNG
from mazelib.mazelib import Maze
from mazelib.generate import AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder, TrivialMaze
from mazelib.solve import BacktrackingSolver, Chain, Collision, Dijkstra, MazeSolveAlgo, RandomMouse, ShortestPath, ShortestPaths, Tremaux

# This code is supposed to pick from the maze generators at random, solve them using specified algorithm, and save the length of the solutions
# and possibly the runtime it took to get the solution. 
# Testing with Sidewinder maze building alg and Tremaux solving alg
######################################################################
# To install mazelib enter "pip install mazelib" into terminal.

m = Maze()
m.generator = Sidewinder(15,15)
# m.generate_entrances()
m.generate()
m.solver = Tremaux()
m.generate_entrances()
m.solve()
print(m)
# showPNG(m.grid)
solution = m.solutions
print(len(solution[0])) # Get length of solution for current solve