
def board_init(coordinates_x, coordinates_y):

    board = [['  ' for _ in range(coordinates_x)] for _ in range(coordinates_y)]
    
    board[0][0] = 'TB'
    board[0][1] = 'HB'
    board[0][2] = 'BB'
    board[0][3] = 'QB'
    board[0][4] = 'KB'
    board[0][5] = 'BB'
    board[0][6] = 'HB'
    board[0][7] = 'TB'

    board[coordinates_y-1][0] = 'TW'
    board[coordinates_y-1][1] = 'HW'
    board[coordinates_y-1][2] = 'BW'
    board[coordinates_y-1][3] = 'QW'
    board[coordinates_y-1][4] = 'KW'
    board[coordinates_y-1][5] = 'BW'
    board[coordinates_y-1][6] = 'HW'
    board[coordinates_y-1][7] = 'TW'

    for i in range(coordinates_x):
        board[1][i] = 'PB'
        board[coordinates_y-2][i] = 'PW'

    return board
