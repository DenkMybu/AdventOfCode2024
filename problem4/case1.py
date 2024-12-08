def find_xmas_in_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    print("rows = {}, cols = {}".format(rows, cols))
    search_word = "XMAS"
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down right diagonal
        (1, -1), # down left diagonal
        (0, -1), # left 
        (-1, 0), # up
        (-1, -1),# up left diagonal
        (-1, 1)  # up right diagonal 
    ]
    count = 0
    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                if find_word(grid, search_word, r, c, rows,cols, direction):
                    count += 1
    return count

def find_word(grid, word, start_row, start_col,rows,cols, direction):
        #print("Start row = {}, start col = {}".format(start_row, start_col))
        for idx in range(len(word)):
            #print("start row = {} + direction[0] * idc = {} * {}".format(start_row, direction[0], idx))
            r = int(start_row + (direction[0] * idx))
            c = int(start_col + (direction[1] * idx))
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (grid[r][c] != word[idx]) :
                return False
        return True

def main():
    print(find_xmas_in_file("list.txt"))
                            

if __name__=="__main__":
    main()