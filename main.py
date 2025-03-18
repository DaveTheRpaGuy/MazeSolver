from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    num_cols = 10
    num_rows = 10
    maze = Maze(10, 10, num_rows, num_cols, 20, 20, win)
    maze.solve()
    win.wait_for_close()

main()