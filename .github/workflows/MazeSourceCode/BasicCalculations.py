# Group 21, Maze Solving AI Source Code
# Connor Thompson, John Huddleston, Aidan Blashe
from display import showPNG
from mazelib.mazelib import Maze
from mazelib.generate import AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder, TrivialMaze
from mazelib.solve import BacktrackingSolver, Chain, Collision, MazeSolveAlgo, RandomMouse, ShortestPath, ShortestPaths, Tremaux
# from mazelib.solve import Dijkstra
import time
# This code is supposed to pick from the maze generators at random, solve them using specified algorithm, and save the length of the solutions
# and possibly the runtime it took to get the solution. 
# Testing with Sidewinder maze building alg and Tremaux solving alg
######################################################################
# To install mazelib enter "pip install mazelib" into terminal.

genAlgorithms = [AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder, TrivialMaze]
solveAlgorithms = [BacktrackingSolver, Chain, Collision, RandomMouse, ShortestPath, ShortestPaths, Tremaux]
# solveAlgorithms.append(Dijkstra)
m = Maze()
m.generator = Division.Division(15,15)
m.generate()
m.generate_entrances()
for solveAlgo in solveAlgorithms:
    solveName = solveAlgo.__name__.split('.')[2]
    m.solver = getattr(solveAlgo, solveName)()
    timeStart = time.time_ns()
    m.solve()
    solveTime = time.time_ns()
    solutionLength = len(m.solutions[0]) # Get length of solution for current solve
    # Time in nanoseconds to solve maze, length of solution
    print(m)
    print(solveName, solveTime - timeStart, solutionLength)
# showPNG(m.grid)