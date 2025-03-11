from cell import Cell
from random import random

class Board:
    def __init__(self, width, height):
        print("init board...")
        self.__width = width
        self.__height = height
        print("board ready")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def setup(self, x, y, n, seed):
        """
        Setup board's n mines with [x,y] as first cell (this cell can't be a mine)

        Parameters:
            x (int): x-index of starting cell
            y (int): y-index of starting cell
            n (int): number of mines on board
            seed (int): seed for reproducibility
        """
        if(n > self.__width * self.__height):
            raise OverflowError('Trying to init more mines than cells')

        # Mines
        self.__seed = seed

        self.__cells = [[Cell()] * self.__width for _ in range(self.__height)]
        random.seed(seed)
        for _ in range (0, n):
            # TODO: avoid potential infinite loop
            [i,j] = [random.uniform(0, self.__width), random.uniform(0, self.__height)]
            while([i,j] == [x,y] and self.__[i][j].value == -1):
                [i,j] = [random.uniform(0, self.__width), random.uniform(0, self.__height)]
            self.__cells[i][j].setMine()

        # Neighboring value
        for i in range(0, self.__width):
            for j in range(0, self.__height):
                # if mine, +1 neighbours value
                if self.__cells[i][j].value == -1:
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            # if neighbour on board range and is not a mine
                            if((dx != 0 or dy != 0) and i+dx >= 0 and i+dx < self.__width and j+dy >= 0 and j+dy < self.__height and self.__cells[i+dx][j+dy].value != -1):
                                self.__cells[i+dx][j+dy].addNeighbourMine()

