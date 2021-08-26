import sys
import pygame
from pygame import draw
from pygame.display import update
import random
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
    cells = []

    def __init__(self, cells, width, height, centerX, centerY):
        self.cells = cells
        self.width = width
        self.height = height
        self.centerX = centerX
        self.centerY = centerY
    
    def setNextState(self):
        for row, cellSet in enumerate(self.cells):
            for col, cell in enumerate(cellSet):
                cell.alive = cell.nextState

    def calcNextState(self):
        for row, cellSet in enumerate(self.cells):
            for col, cell in enumerate(cellSet):
                cell.aliveNext = 0
                if cell.u != None:
                    if cell.u.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.d != None:
                    if cell.d.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.l != None:
                    if cell.l.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.r != None:
                    if cell.r.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.rUp != None:
                    if cell.rUp.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.rDown != None:
                    if cell.rDown.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.lUp != None:
                    if cell.lUp.alive:
                        cell.aliveNext = cell.aliveNext + 1
                if cell.lDown != None:
                    if cell.lDown.alive:
                        cell.aliveNext = cell.aliveNext + 1
        
        for row, cellSet in enumerate(self.cells):
            for col, cell in enumerate(cellSet):
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
                # Condición de borde Up, Down
                if row > 0:
                    cell.u = self.cells[row - 1][col]
                if row < lastRow:
                    cell.d = self.cells[row + 1][col]
                # Condición rDown
                if row < lastRow and col < lastCol:
                    cell.rDown = self.cells[row + 1][col + 1]
                # Condición lDown
                if row < lastRow and col > 0:
                    cell.lDown = self.cells[row + 1][col - 1]
                # Condición rUp
                if row > 0 and col < lastCol:
                    cell.rUp = self.cells[row - 1][col + 1]
                # Condición lUp
                if row > 0 and col > 0:
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

#---#
cells = []
for _i in range(const.BSIZE):
    cellSet = []
    for _j in range(const.BSIZE):
        cellSet.append(Cell(False, 20, 20))
    cells.append(cellSet)

board = Board(cells, const.BSIZE, const.BSIZE, 100, 100)
board.calcReferences()

""" for i in range(1000):
    r1 = random.randint(0,const.BSIZE - 1)
    r2 = random.randint(0,const.BSIZE - 1)
    board.cells[r1][r2].alive = True """

#patterns.setupGosperGliderGun(board)
#patterns.setUpMix(board)
patterns.setUpDefault(board)

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
