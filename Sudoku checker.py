
DESIRED_SUM = 1+2+3+4+5+6+7+8+9
INVALID_GRID = [[1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9],
                    [1,2,3,4,5,6,7,8,9]]

VALID_GRID = [[4,3,5,2,6,9,7,8,1],
              [6,8,2,5,7,1,4,9,3],
              [1,9,7,8,3,4,5,6,2],
              [8,2,6,1,9,5,3,4,7],
              [3,7,4,6,8,2,9,1,5],
              [9,5,1,7,4,3,6,2,8],
              [5,1,9,3,2,6,8,7,4],
              [2,4,8,9,5,7,1,3,6],
              [7,6,3,4,1,8,2,5,9]]

def check_sudoku(sudoku_grid):
    if check_rows(sudoku_grid) == True:
        print ("rows look good")
        if check_columns(sudoku_grid) == True:
            print ("colums look good")
            if check_squares(sudoku_grid) == True:
                print ("squares look good")
                return True

def check_rows(grid):
    for row in grid:
        if is_valid_row(row) == False:
            return False
    return True

def is_valid_row(row):
    required_numbers = [1,2,3,4,5,6,7,8,9]
    for number in required_numbers:
            #print(row)
            #print(number)
            if number not in row:
                return False
    return True

def check_columns(grid):
    x=-1
    required_numbers = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    terms = [] #allocating numbers

    for p in range (1,10):
        x=x+1
        del terms[:]
        for row in grid:
            var = row[x:x+1]
            terms.append(var)
        for number in required_numbers:
            if number not in terms:
                return False
    return True 

def check_squares(grid):
    required_numbers = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    terms = [] #allocating numbers

    for p in range (0,9,3):
        del terms[:]
        for row in grid:
            terms.append(row[p:p+1])
            terms.append(row[p+1:p+2])
            terms.append(row[p+2:p+3])
        for number in required_numbers:
            if number not in terms[0:9]:
                return False
            if number not in terms[9:18]:
                return False
            if number not in terms[18:28]:
                return False
    return True  

print (check_sudoku(VALID_GRID))