class Cell:
    def __init__(self):
        self.__value = 0;
        self.__state = ""
    
    @property
    def value(self):
        """
        Indicates cell contained value
        - -1: mine
        - 0: nothing
        - 1-8: number
        """
        return self.__value

    def setMine(self):
        self.__value = -1;
