def initialize_board(height, length):
    board = []
    for i in range(height):
        rows = []
        for j in range(length):
            rows.append('-')
        board.append(rows)
    return board


def print_board(board):
    for row in reversed(board):
        for col in row:
            print(col, end=' ')
        print()


def insert_chip(board, col, chip_type):
    for i in range(0, height):
        if board[i][col] == '-':
            board[i][col] = chip_type
            row = i
            return row


def check_if_winner(board, col, row, chip_type):
    rowCount = 0
    for i in range(0, len(board[row])):
        if board[row][i] == chip_type:
            rowCount = rowCount + 1
            if rowCount == 4:
                return True
        else:
            rowCount = 0

    colCount = 0
    for i in range(0, len(board)):
        if board[i][col] == chip_type:
            colCount = colCount + 1
            if colCount == 4:
                return True
        else:
            colCount = 0


def tie_game():
    k = 0
    for i in range(0, height):
        if '-' not in board[i]:
            k = k + 1
            if k == height:
                return False
        if '-' in board[i]:
            k = 0


if __name__ == '__main__':

    height = int(input('What would you like the height of the board to be? '))
    length = int(input('What would you like the length of the board to be? '))
    board = initialize_board(height, length)
    row = height
    col = length
    (print_board(board))
    chip_type = ''
    col = ''

    print('\nPlayer 1: x')
    print('Player 2: o')

    x = 0
    player = 1
    chip_type = 'x'
    row = 0
    game = True
    while game:

        col = int(input(f'\nPlayer {player}: Which column would you like to choose? '))
        row = insert_chip(board, col, chip_type)

        print_board(board)

        if check_if_winner(board, col, row, chip_type) == True:
            print(f'\nPlayer {player} won the game!')
            game = False

        if tie_game() == False:
            print('Draw. Nobody wins.')
            game = False

        player = 2 if player == 1 else 1
        chip_type = 'o' if chip_type == 'x' else 'x'


