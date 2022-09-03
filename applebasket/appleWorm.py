from appleEater import AppleEater

class AppleWorm(AppleEater):
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



