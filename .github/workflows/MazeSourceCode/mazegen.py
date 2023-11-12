# Group 21, Maze Solving AI Source Code
# Connor Thompson, John Huddleston, Aidan Blashe
# Imports
from display import showPNG
from mazelib.mazelib import Maze
from mazelib.generate.Sidewinder import Sidewinder
from mazelib.solve.Tremaux import Tremaux
m = Maze()
m.generator = Sidewinder(24,33)
# m.generate_entrances()
m.generate()
m.solver = Tremaux()
showPNG(m.grid)