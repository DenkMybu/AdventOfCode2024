def find_xmas_in_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    print("rows = {}, cols = {}".format(rows, cols))
    search_word = "MAS"
    inv_word = "SAM"
    count = 0
    for r in range(rows):
        for c in range(cols):
            if find_both_words(grid, search_word,inv_word, r, c, rows, cols):
                count += 1
    return count

def find_both_words(grid, word,inv_word, r, c,rows,cols):
        if (r+2) < 0 or (r+2) >= rows or (c+2) < 0 or (c+2) >= cols:
            return False
        if grid[r+1][c+1] != "A":
            return False  
        down_right = str(grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2])
        up_left = str(grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2])
        if (down_right == word or down_right==inv_word) and (up_left == word or up_left == inv_word):
            return True
        return False
def main():
    print(find_xmas_in_file("list.txt"))                    
if __name__=="__main__":
    main()