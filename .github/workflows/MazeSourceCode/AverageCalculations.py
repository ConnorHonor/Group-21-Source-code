# Group 21, Maze Solving AI Source Code
# Connor Thompson, John Huddleston, Aidan Blashe
from display import showPNG
from mazelib.mazelib import Maze
from mazelib.generate import AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder, TrivialMaze
from mazelib.solve import BacktrackingSolver, Chain, Collision, MazeSolveAlgo, RandomMouse, ShortestPath, ShortestPaths, Tremaux
import time
# This code solves mazes using every generation and solving algorithm, collecting the time it took to solve using each solving method.
# Prints once its done solving a maze
# Link to google sheets with maze representation maker and the average time graph. Paste the printed graph into the first sheet and see the graph in the second sheet.
# https://1drv.ms/x/s!AiSBEN1snTvR1yJz3jfkzML69t1k?e=waQVAX
######################################################################
# To install mazelib enter "pip install mazelib" into terminal.

genAlgorithms = [AldousBroder, BacktrackingGenerator, BinaryTree, CellularAutomaton, Division, DungeonRooms, Ellers, GrowingTree, HuntAndKill, Kruskal, Prims, Sidewinder]
solveAlgorithms = [BacktrackingSolver, Chain, RandomMouse, ShortestPath, ShortestPaths, Tremaux]
# solveAlgorithms.append(Dijkstra)
solveTimes = {}
for genAlg in genAlgorithms:
    for i in range(5):
        # Create a unique maze using the algorithm
        m = Maze()
        genName = genAlg.__name__.split('.')[2]
        # Can change size of maze currently set to 15 by 15 hallways
        m.generator = getattr(genAlg, genName)(15,15)
        m.generate()
        m.generate_entrances()
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
            # Output every finished solution so you know where its at in the list
            print(genName, solveName, solveTime - timeStart, solutionLength)

for solveAlg in solveTimes.keys():
    total = 0
    items = 0
    for timeInSeconds in solveTimes[solveAlg]:
        items+=1
        total+=timeInSeconds
    average = total/items
    print(solveAlg, average)
# showPNG(m.grid)