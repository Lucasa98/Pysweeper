class Cell:
    def __init__(self):
        self.__value = 0;
        self.__state = "hide"
    
    @property
    def value(self):
        """
        Indicates cell contained value
        - -1: mine
        - 0: nothing
        - 1-8: number
        """
        return self.__value
    
    def set(self, value):
        self.__value = value

    def setMine(self):
        """
        Set this cell as a mine
        """
        self.__value = -1

    def leftClick(self):
        if self.__state != "flag":
            self.__state = "show"
        return self.__value
    
    def rightClick(self):
        if self.__state != "show":
            self.__state = "flag" if self.__state == "hide" else "hide"
        return self.__value

    def addNeighbourMine(self):
        self.__value = self.__value + 1