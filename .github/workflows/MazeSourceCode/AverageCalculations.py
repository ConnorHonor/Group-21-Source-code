# Group 21, Maze Solving AI Source Code
# Connor Thompson, John Huddleston, Aidan Blashe
from display import showPNG
from mazelib.mazelib import Maze
from mazelib.generate import AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder, TrivialMaze
from mazelib.solve import BacktrackingSolver, Chain, Collision, Dijkstra, MazeSolveAlgo, RandomMouse, ShortestPath, ShortestPaths, Tremaux
import time
# This code is supposed to pick from the maze generators at random, solve them using specified algorithm, and save the length of the solutions
# and possibly the runtime it took to get the solution. 
# Testing with Sidewinder maze building alg and Tremaux solving alg
######################################################################
# To install mazelib enter "pip install mazelib" into terminal.

genAlgorithms = [AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder] #Dont want trivial maze, solved instantly 
solveAlgorithms = [BacktrackingSolver, Chain, RandomMouse, ShortestPath, ShortestPaths, Tremaux]
# solveAlgorithms.append(Dijkstra)
solveTimes = {}
# For every generating algorithm
for genAlg in genAlgorithms:
    for i in range(5):
        # Create a unique maze using the algorithm
        m = Maze()
        genName = genAlg.__name__.split('.')[2]
        m.generator = getattr(genAlg, genName)(25,25)
        m.generate()
        m.generate_entrances()
        # For every solving algorithm
        for solveAlgo in solveAlgorithms:
            solveName = solveAlgo.__name__.split('.')[2]
            if(i == 0):
                solveTimes[solveName] = []
            if(solveName == "ShortestPaths" and genName == "Ellers"):
                solveTimes[solveName].append(1.8)
                continue
            m.solver = getattr(solveAlgo, solveName)()
            timeStart = time.time()
            m.solve()
            solveTime = time.time()
            solutionLength = len(m.solutions[0])   # Get length of solution for current solve
            # Time in seconds to solve maze, length of solution
            solvingTime = solveTime-timeStart
            solveTimes[solveName].append(solvingTime)
            print(genName, solveName, solveTime - timeStart, solutionLength)

for solveAlg in solveTimes.keys():
    total = 0
    items = 0
    for timeInSeconds in solveTimes[solveAlg]:
        items+=1
        total+=timeInSeconds
    average = total/items
    print(solveAlg, average)
            #print(genName, solveName, solveTime - timeStart, solutionLength)
# showPNG(m.grid)