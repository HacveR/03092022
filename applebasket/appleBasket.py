#  DATA CLASSES implementation recommended


class AppleBasket():
    ''' CLASS: CREATE (OBJECT) WITH ONE (INT) VALUE  '''


    def __init__(self):
        ''' CONSTRACTOR: INITIALIZE (INT) STOCK, SET TO 0 '''
        self.stock = 0




    def searchForApple(self):
        ''' BOOLEAN FUNCTION: RETURN TRUE IF STACK > 0, OR FALSE  '''
        if self.getStock() > 0:
            return True
        else:
            return False


    def getStock(self):
        ''' GETTER: RETURN (INT) VALUE '''
        return self.stock



    def addApple(self):
        ''' SETTER: UPDATE BY 1 '''
        self.stock += 1



    def addApples(self,number):
        ''' SETTER: TAKE ONE (INT) PARAMETERS '''
        if isinstance(number, int):
            if number > 0:
                self.stock += number



    def takeApple(self):
        ''' SETTER: UPDATE BY -1 '''
        if self.getStock() > 0:
            self.stock -= 1



    def takeApples(self, number):
        ''' SETTER: TAKE ONE (INT) PARAMETERS '''
        if isinstance(number, int):
            if number < 0:
                pass
            elif number >= self.getStock():
                self.stock = 0
            else:
                self.stock -= number

