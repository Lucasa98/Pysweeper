from board import Board

class Game:
    def __init__(self, width = 32, height = 24, minesCount = 20, seed = 10):
        """
        Initialize a game

        Parameters:
            width (int): width of the board (Default 32)
            height (int): height of the board (Default 24)
            minesCount (int): number of mines on the board (Default 20)
            seed (int): starting seed (Default 10)
        """
        print("init game...")
        self.__minesCount = minesCount
        self.__board = Board(width, height)
        self.__seed = seed
        print("game ready")

    def start(self, x, y, seed = 0):
        """
        Start a game. It's meant to start clicking on a cell for the first time

        Parameters:
            x (int): first clicked cell x-coordinate
            y (int): first clicked cell y-coordinate
            seed (int): starting seed (0 to restart with same seed)
        """
        self.__seed = seed if seed != 0 else self.__seed
        self.__board.setup(x, y, self.__minesCount, self.__seed)