from window import *
from line import *
from point import *

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(5, 5), Point(50, 50)), "red")
    win.draw_line(Line(Point(5, 50), Point(50, 5)), "green")
    win.wait_for_close()

main()