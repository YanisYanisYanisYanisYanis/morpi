import random


def print_grid(grid):
    for el in grid:
        res = "["
        for i in range (len(el)-1):
            res += str(el[i]) + " "
        res += str(el[len(el)-1])
        res += "]"
        print(res)

def generate_grid(n):
    result = []
    for _ in range (n):
        result.append([0] * n)
    return result

def randomize_grid(grid):
    for el in grid :
        for i in range (len(el)):
            el[i] = random.randint(0,2)

def add_pattern(x_start,y_start,pattern,grid):
    for i in range (len(pattern)):
        for j in range (len(pattern[i])):
            if pattern[i][j] >= 0:
                grid[y_start+i][x_start+j] = pattern[i][j]


if __name__ == "__main__" :
    grid = generate_grid(5)
    pattern = [
        [1,2,3],
        [4,5,6]
    ]
    randomize_grid(grid)
    add_pattern(1,1,pattern,grid)
    print_grid(grid)
