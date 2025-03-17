from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_bottom_wall = False
    cell1.has_right_wall = False
    cell1.draw(1, 1, 20, 20)
    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell2.has_left_wall = False
    cell2.draw(21, 1, 40, 20)
    cell3 = Cell(win)
    cell3.has_top_wall = True
    cell3.has_right_wall = False
    cell3.draw(1, 21, 20, 40)
    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.draw(21, 21, 40, 40)
    cell1.draw_move(cell2)
    cell2.draw_move(cell4, True)
    #win.draw_line(Line(Point(5, 5), Point(50, 50)), "red")
    #win.draw_line(Line(Point(5, 50), Point(50, 5)), "green")
    win.wait_for_close()

main()