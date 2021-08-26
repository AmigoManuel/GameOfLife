def setUpDefault(board):
    board.cells[5][6].alive = True
    board.cells[5][5].alive = True
    board.cells[4][5].alive = True
    board.cells[6][5].alive = True
    board.cells[4][4].alive = True

def setUpMix(board):
    board.cells[0][12].alive = True
    board.cells[1][12].alive = True
    board.cells[2][12].alive = True
    board.cells[1][6].alive = True
    board.cells[2][7].alive = True
    board.cells[0][8].alive = True
    board.cells[1][8].alive = True
    board.cells[2][8].alive = True

def setUpGosperGliderGun(board):
    board.cells[5][1].alive = True
    board.cells[5][2].alive = True
    board.cells[6][1].alive = True
    board.cells[6][2].alive = True
    board.cells[5][11].alive = True
    board.cells[6][11].alive = True
    board.cells[7][11].alive = True
    board.cells[4][12].alive = True
    board.cells[3][13].alive = True
    board.cells[3][14].alive = True
    board.cells[8][12].alive = True
    board.cells[9][13].alive = True
    board.cells[9][14].alive = True
    board.cells[6][15].alive = True
    board.cells[4][16].alive = True
    board.cells[5][17].alive = True
    board.cells[6][17].alive = True
    board.cells[7][17].alive = True
    board.cells[6][18].alive = True
    board.cells[8][16].alive = True
    board.cells[3][21].alive = True
    board.cells[4][21].alive = True
    board.cells[5][21].alive = True
    board.cells[3][22].alive = True
    board.cells[4][22].alive = True
    board.cells[5][22].alive = True
    board.cells[2][23].alive = True
    board.cells[6][23].alive = True
    board.cells[1][25].alive = True
    board.cells[2][25].alive = True
    board.cells[6][25].alive = True
    board.cells[7][25].alive = True
    board.cells[3][35].alive = True
    board.cells[4][35].alive = True
    board.cells[3][36].alive = True
    board.cells[4][36].alive = True
