# solving soduku solution by using python
 
# creating the board
def create_board(arr):
    for i in range(9):
        for j in range(9):
            print (arr[i][j], end = " "),
        print ()
 
         
# It should accept a 2D-array as a parameter 
# and return true if it is a valid or 
# false if it is invalid. 
# The array is populated with 
# integers ranging from 0 to 9
def find_empty_cell(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False
 
#if the given number assigned 
# to specified row return True or False
def check_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False
 
# Return True if assigned number
# in the specified column matches
# the given number.
def check_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False
 
# Returns True or False if any assigned entry
# within the specified 3x3 block
# matches the given number
def check_in_block(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False
 
# checking the number assigning to the given row,col
# Returns a boolean which indicates
# whether it will be correct to assign
# num to the given row, col location.
def check_cell_is_valid(arr, row, col, num):
     
    # Check if 'num' is not already
    # placed in current row,
    # current column and current 3x3 box
    return (not check_in_row(arr, row, num) and
           (not check_in_col(arr, col, num) and
           (not check_in_block(arr, row - (row % 3),
                           col - (col % 3), num))))
 
# Takes a partially filled-in grid
# and attempts to assign values to
# all unassigned locations in such a
# way to meet the requirements
# for Sudoku solution (non-duplication
# across rows, columns, and boxes)
def soduko_solution(arr, r1, c1):
     
    # 'l' is a list variable that keeps the
    # record of row and col in
    # find_empty_location Function   
    #l =[0, 0]
     
    # If there is no unassigned
    # location, we are done   
    # if(not find_empty_location(arr, l)):
    #     return True
     
    # Assigning list values to row and col
    # that we got from the above Function
    row = r1
    col = c1
    
    if (row == 8 and col == 9):
        return True

    if col == 9:
        row += 1
        col = 0
        
    if arr[row][col] > 0:
        return soduko_solution(arr, row, col + 1)
    # consider digits 1 to 9
    for num in range(1, 10):
         
        # if looks promising
        if(check_cell_is_valid(arr,
                          row, col, num)):
             
            # make tentative assignment
            arr[row][col]= num
 
            # return, if success,
            # ya !
            if(soduko_solution(arr, row, col+1)):
                return True
 
            # failure, unmake & try again
            arr[row][col] = 0
             
    # this triggers backtracking       
    return False
 
# Driver main function to test above functions
if __name__=="__main__":
     
    # creating a 2D array for the grid
    board =[[0 for x in range(9)]for y in range(9)]
     
    # assigning values to the grid
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    # if success print the grid
    if(soduko_solution(board, 0, 0)):
        create_board(board)
    else:
        print ("No solution exists")