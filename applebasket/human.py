from appleEater import AppleEater

class Human(AppleEater):
    ''' CLASS:  CREATE (OBJECT) WITH ONE NAME VALUE  '''


    def __init__(self,name):
        ''' CONSTRACTOR: ONE PARAMETER NAME '''
        self.name = name

    def __str__(self) -> str:
        '''MAGIC METHOD: REPLACE PHISICAL ADDRESS WITH SELF.NAME'''
        return f"{self.name}"






    def eating(self,foodSource):
        ''' CALL TAKEAPPLE() FUNCTION FORM FOODSOURCE INSTANCE'''
        foodSource.takeApple()



    def getName(self):
        ''' GETTER: RETURN THE NAME'''
        return self.name



    def setName(self,name):
        ''' SETTER: SET THE NAME '''
        self.name = name




