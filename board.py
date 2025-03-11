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

        self.__seed = seed

        self.__cells = [[Cell()] * self.__width for _ in range(self.__height)]
        random.seed(seed)
        for _ in range (0, n):
            # TODO: avoid potential infinite loop
            [i,j] = [random.uniform(0, self.__width), random.uniform(0, self.__height)]
            while([i,j] == [x,y] and self.__[i][j].value == -1):
                [i,j] = [random.uniform(0, self.__width), random.uniform(0, self.__height)]
            self.__cells[i][j].setMine()
