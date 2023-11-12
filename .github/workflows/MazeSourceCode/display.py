# This code is from the mazelib library by John Stilley
# May change this to also show PNG of the solution squares and start / end square
# Currently just shows the maze with black and white squares
import matplotlib.pyplot as plt

def showPNG(grid):
    """Generate a simple image of the maze."""
    plt.figure(figsize=(10, 5))
    plt.imshow(grid, cmap=plt.cm.binary, interpolation='nearest')
    plt.xticks([]), plt.yticks([])
    plt.show()