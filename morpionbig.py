from grid_generator import *

def game():
    grid_size = get_grid_size()
    win_cond = get_win_cond(grid_size)
    players = get_players()

    grid = generate_grid(grid_size)
    # pattern = [[0, 1, 1, 1], [1, 0, 0, 0]]
    # add_pattern(0,0,pattern,grid)
    print_grid(grid)

    is_won = False

    while not is_won:
        for player in players:
            is_won = player_move(grid, player, win_cond)
            if is_won:
                print(f'Player {player} wins!')
                break
            if check_tie(grid):
                print("It's a tie!")
                return
            
def get_grid_size():
    return int(input("Grid size? "))

def get_win_cond(grid_size):
    while True:
        win_cond = int(input("How many in a row to win? "))
        if win_cond <= grid_size:
            return win_cond
        print("The grid is too small for so many symbols in a row!")

def get_players():
    n = int(input('How many players? '))
    return list(range(1, n + 1))

def player_move(grid, player, win_cond):
    check_move(grid, player)
    is_won = check_win(grid, player, win_cond)
    return is_won

def check_tie(grid):
    return all(cell != 0 for row in grid for cell in row)

def check_move(grid, player):
    while True:
        x_string, y_string = input(
            "Player {} enter the coordinates of your move :".format(player)
        ).split(",")
        x, y = int(x_string), int(y_string)
        if grid[x - 1][y - 1] == 0:
            grid[x - 1][y - 1] = player
            print_grid(grid)
            break
        else:
            print("This space is not free!")

def check_win(grid, player, win_cond):
    is_won = (
        check_row(grid, player, win_cond)
        or check_col(grid, player, win_cond)
        or check_diag1(grid, player, win_cond)
        or check_diag2(grid, player, win_cond)
    )
    return is_won

def check_row(grid, player, win_cond):
    for row in range(len(grid)):
        for col in range(len(grid[row]) - win_cond + 1):
            if all(grid[row][col + i] == player for i in range(win_cond)):
                return True

def check_col(grid, player, win_cond):
    for row in range(len(grid) - win_cond + 1):
        for col in range(len(grid[row])):
            if all(grid[row + i][col] == player for i in range(win_cond)):
                return True

def check_diag1(grid, player, win_cond):
    # diagonal 1
    for row in range(len(grid) - win_cond + 1):
        for col in range(len(grid[row]) - win_cond + 1):
            if all(grid[row + i][col + i] == player for i in range(win_cond)):
                return True

def check_diag2(grid, player, win_cond):
    # diagonal 2
    for row in range(len(grid) - win_cond + 1):
        for col in range(len(grid[row])):
            if all(grid[row + i][col - i] == player for i in range(win_cond)):
                return True