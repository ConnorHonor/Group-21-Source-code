# Group 21, Maze Solving AI Source Code
# Connor Thompson, John Huddleston, Aidan Blashe
# Imports
from display import showPNG
from mazelib.mazelib import Maze
from mazelib.generate.Sidewinder import Sidewinder
from mazelib.solve.Tremaux import Tremaux
# This code is supposed to pick from the maze generators at random, solve them using specified algorithm, and save the length of the solutions 
# and possibly the runtime it took to get the solution. 
# Testing with Sidewinder maze building alg and Tremaux solving alg
######################################################################
# To install mazelib enter "pip install mazelib" into terminal.

m = Maze()
m.generator = Sidewinder(24,33)
# m.generate_entrances()
m.generate()
m.solver = Tremaux()
m.generate_entrances()
m.solve()
print(m)
showPNG(m.grid)