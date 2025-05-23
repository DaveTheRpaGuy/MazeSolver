import time, random

from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            cell_column = []
            for j in range(self._num_rows):
                cell_column.append(Cell(self._win))
            self._cells.append(cell_column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + (j * self._cell_size_y)
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        #time.sleep(0.05)
        #time.sleep(.1)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = self._get_unvisited_nearby_cells(i, j)
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            try:
                direction = random.randrange(len(to_visit))
            except:
                print(f"randrange next with input: {len(to_visit)}")
                raise
            new_i = to_visit[direction][0]
            new_j = to_visit[direction][1]
            new_cell = self._cells[new_i][new_j]
            if i > new_i:
                current_cell.has_left_wall = False
                new_cell.has_right_wall = False
            elif j > new_j:
                current_cell.has_top_wall = False
                new_cell.has_bottom_wall = False
            elif j < new_j:
                current_cell.has_bottom_wall = False
                new_cell.has_top_wall = False
            else:
                current_cell.has_right_wall = False
                new_cell.has_left_wall = False
            self._break_walls_r(new_i, new_j)
            
    def _get_unvisited_nearby_cells(self, i, j):
        cells = []
        if i > 0 and self._cells[i-1][j].visited == False:
            cells.append((i-1, j))
        if j > 0 and self._cells[i][j-1].visited == False:
            cells.append((i, j-1))
        if i < self._num_cols-1 and self._cells[i+1][j].visited == False:
            cells.append((i+1, j))
        if j < self._num_rows-1 and self._cells[i][j+1].visited == False:
            cells.append((i, j+1))
        return cells

    def _reset_cells_visited(self):
        for cell_column in self._cells:
            for cell in cell_column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i >= self._num_cols-1 and j >= self._num_rows-1:
            return True
        if i > 0 and not self._cells[i-1][j].visited and not current_cell.has_left_wall:
            current_cell.draw_move(self._cells[i-1][j])
            result = self._solve_r(i-1, j)
            if result:
                return True
            else:
                current_cell.draw_move(self._cells[i-1][j], True)
        if j > 0 and not self._cells[i][j-1].visited and not current_cell.has_top_wall:
            current_cell.draw_move(self._cells[i][j-1])
            result = self._solve_r(i, j-1)
            if result:
                return True
            else:
                current_cell.draw_move(self._cells[i][j-1], True)
        if i < self._num_cols-1 and not self._cells[i+1][j].visited and not current_cell.has_right_wall:
            current_cell.draw_move(self._cells[i+1][j])
            result = self._solve_r(i+1, j)
            if result:
                return True
            else:
                current_cell.draw_move(self._cells[i+1][j], True)
        if j < self._num_rows-1 and not self._cells[i][j+1].visited and not current_cell.has_bottom_wall:
            current_cell.draw_move(self._cells[i][j+1])
            result = self._solve_r(i, j+1)
            if result:
                return True
            else:
                current_cell.draw_move(self._cells[i][j+1], True)
        return False
        