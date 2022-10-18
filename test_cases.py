import unittest
from Scaniasudokutest.sudoku import *

sudoku_sample = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]

class SudukoTest(unittest.TestCase):
    def test_check_in_row(self):
        self.assertTrue(not check_in_row(sudoku_sample,1,8))

    def test_used_in_col(self):
        self.assertTrue(not check_in_col(sudoku_sample,1,5))
    
    def test_used_in_box(self):
        self.assertTrue(check_in_block(sudoku_sample,3,3,6))

if __name__=="__main__":
    unittest.main()