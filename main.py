import sys
import pygame
from pygame import draw
from pygame.display import update
import constants as const
import patterns

pygame.init()

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(const.WSIZE)


class Cell:
    def __init__(self, alive, width, height):
        self.alive = alive
        self.width = width
        self.height = height
        # locations
        self.u, self.d, self.l, self.r = None, None, None, None
        # locations_2
        self.rUp, self.rDown, self.lUp, self.lDown = None, None, None, None
        self.nextState = False
        self.aliveNext = 0

    def drawCell(self, screen, x, y):
        if self.alive:
            pygame.draw.rect(
                screen, const.WHITE, [x, y, self.width-2, self.height-2])
        else:
            pygame.draw.rect(
                screen, const.WHITE, [x, y, self.width, self.height], 2)


class Board:
    def __init__(self, cells, width, height, centerX, centerY):
        self.cells = cells
        self.width = width
        self.height = height
        self.centerX = centerX
        self.centerY = centerY
    
    def setNextState(self):
        for cellSet in self.cells:
            for cell in cellSet:
                cell.alive = cell.nextState

    def calcNextState(self):
        for cellSet in self.cells:
            for cell in cellSet:
                cell.aliveNext = 0
                if cell.u != None and cell.u.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.d != None and cell.d.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.l != None and cell.l.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.r != None and cell.r.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.rUp != None and cell.rUp.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.rDown != None and cell.rDown.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.lUp != None and cell.lUp.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.lDown != None and cell.lDown.alive:
                        cell.aliveNext = cell.aliveNext + 1
        # Conditions
        for cellSet in self.cells:
            for cell in cellSet:
                if cell.alive:
                    # Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.
                    if cell.aliveNext == 2 or cell.aliveNext == 3:
                        cell.nextState = True
                    # Si una célula está viva y tiene más de tres vecinas vivas, muere.
                    else:
                        cell.nextState = False
                # Si una célula está muerta y tiene tres vecinas vivas, nace.
                else:
                    if cell.aliveNext == 3:
                        cell.nextState = True
                    else:
                        cell.nextState = False

    def calcReferences(self):
        for row, cellSet in enumerate(self.cells):
            for col, cell in enumerate(cellSet):
                lastCol = len(cellSet) - 1
                lastRow = len(self.cells) - 1
                # Condición de borde Left, Rigth
                if col < lastCol:
                    cell.r = cellSet[col + 1]
                if col > 0:
                    cell.l = cellSet[col - 1]
                # Condición de borde Down
                if row < lastRow:
                    cell.d = self.cells[row + 1][col]
                    # Condición rDown
                    if col < lastCol:
                        cell.rDown = self.cells[row + 1][col + 1]
                    # Condición lDown
                    if col > 0:
                        cell.lDown = self.cells[row + 1][col - 1]
                # Condición de borde Up
                if row > 0:
                    cell.u = self.cells[row - 1][col]
                    # Condición rUp
                    if col < lastCol:
                        cell.rUp = self.cells[row - 1][col + 1]
                    # Condición lUp
                    if col > 0:
                        cell.lUp = self.cells[row - 1][col - 1]

    def drawBoard(self, screen):
        x, y = self.centerX, self.centerY
        for cellSet in self.cells:
            for countCell, cell in enumerate(cellSet):
                cell.drawCell(screen, x, y)
                x = x + cell.width
                if countCell == self.width - 1:
                    x = self.centerX
                    y = y + cell.height

# Init Cells
cells = []
for _ in range(const.BSIZE):
    cellSet = []
    for _ in range(const.BSIZE):
        cellSet.append(Cell(False, 10, 10))
    cells.append(cellSet)

# Init Board
board = Board(cells, const.BSIZE, const.BSIZE, 100, 100)

# Calculate References to other cells
board.calcReferences()

# Beauty patterns
#patterns.setUpDefault(board)
#patterns.setUpMix(board)
patterns.setUpGosperGliderGun(board)

# Execute game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(const.BLACK)
    board.drawBoard(screen)
    board.calcNextState()
    board.setNextState()

    pygame.display.update()
    fpsClock.tick(const.FPS)
