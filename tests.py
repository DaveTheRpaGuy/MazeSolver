import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_equal_cols_and_rows_and_offset(self):
        num_cols = 20
        num_rows = 20
        maze_x1 = 10
        maze_y1 = 10
        m1 = Maze(maze_x1, maze_y1, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            m1._x1,
            maze_x1
        )
        self.assertEqual(
            m1._x1,
            maze_y1
        )

    def test_maze_create_cells_large_cell_size(self):
        num_cols = 10
        num_rows = 10
        maze_x1 = 0
        maze_y1 = 0
        cell_size = 50
        m1 = Maze(maze_x1, maze_y1, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(
            m1._cell_size_x,
            cell_size
        )
        self.assertEqual(
            m1._cell_size_y,
            cell_size
        )
    
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_cols-1][num_rows-1].has_bottom_wall)
        

if __name__ == "__main__":
    unittest.main()