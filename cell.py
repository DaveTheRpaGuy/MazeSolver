from point import Point
from line import Line
from window import Window

class Cell:
    def __init__(self, win):
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            line.draw(self._win.canvas, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            line.draw(self._win.canvas, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            line.draw(self._win.canvas, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            line.draw(self._win.canvas, "black")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        line = Line(
            self.get_center_point(),
            to_cell.get_center_point()
            )
        self._win.draw_line(line, color)
        
    def get_center_point(self):
        center_x = self._x2 - ((self._x2 - self._x1) / 2)
        center_y = self._y2 - ((self._y2 - self._y1) / 2)
        return Point(center_x, center_y)