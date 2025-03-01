from yanis22 import *


grid_size = int(input('Grid size? '))
while True:
    win_cond = int(input("How many in a row to win? "))
    if win_cond <= grid_size:
        break
    else:
        print('The grid is too small for so many symbols in a row!')
players = [1,2]


def game():
    is_won = False
    grid = generate_grid(grid_size)
    pattern = [[0,1,1,1],[1,0,0,0]]
    # add_pattern(0,0,pattern,grid)
    print_grid(grid)
    while not is_won:
        for player in players:
            is_won = player_move(grid, player)
            if is_won:
                break
    

def player_move(grid, player):
    check_empty(grid, player)
    is_won = check_win(grid, player, win_cond)
    return is_won


def check_empty(grid, player):
    while True:
        x_string,y_string = input('Player {} enter the coordinates of your move :'.format(player)).split(',')
        x,y = int(x_string),int(y_string)
        if grid[x-1][y-1] == 0:
            grid[x-1][y-1] = player
            print_grid(grid)
            break
        else:
            print('This space is not free!')


def check_win(grid, player, win_cond):
    is_won = check_row(grid, player, win_cond) or check_col(grid, player, win_cond) or check_diag1(grid, player) or check_diag2(grid, player)
    return is_won


def check_row(grid, player, win_cond):
    for row in range(len(grid)):
        for col in range(len(grid[row]) - win_cond + 1):
            if all(grid[row][col + i] == player for i in range(win_cond)):
                print(player, 'has won (row', row + 1, ')')
                return True

def check_col(grid, player, win_cond):
    for row in range(len(grid) - win_cond + 1):
        for col in range(len(grid[row])):
            if all(grid[row + i][col] == player for i in range(win_cond)):
                print(player, 'has won (col', col + 1, ')')
                return True

def check_diag1(grid, player):
    # diagonal 1
    for row in range(len(grid) - win_cond + 1):
        for col in range(len(grid[row]) - win_cond + 1):
            if all(grid[row + i][col + i] == player for i in range (win_cond)):
                print(player, 'has won (diagonal)')
                return True

def check_diag2(grid, player):
    # diagonal 2
    for row in range(len(grid) - win_cond + 1):
        for col in range(len(grid[row])):
            if all(grid[row + i][col - i] == player for i in range(win_cond)):
                print(player, 'has won (diagonal)')
                return True


if __name__ == '__main__':
    game()