from appleEater import AppleEater
import random


class AppleMold(AppleEater):
    ''' CLASS:  CREATE (OBJECT) WITH ONE NAME VALUE  '''


    def __init__(self):
        ''' CONSTRACTOR: INITIALIZE NAME, SET TO "MR MOLDY" '''
        self.name = "Mr Moldy"

    def __str__(self) -> str:
        '''MAGIC METHOD: REPLACE PHISICAL ADDRESS WITH SELF.NAME'''
        return f"{self.name}"




    def justThrowAnError(self,number):
        ''' DUMMY METHOD FOR PYTEST'''
        if isinstance(number, int):
            if number > 10:
                raise ValueError(" Bigger than 10")
            else:
                raise ValueError(" Smaller than 10")



    def eating(self,foodSource):
        ''' RECURSIVE FUNCTION:  TAKING AS A PARAMETER INSTANCE OF AN ANOTHER OBJECT '''

        if self.appleSearch(foodSource):
            print("     Another apple turned moldy")
#           Updating value of a stock
            foodSource.takeApple()

#           TRUE/FALSE check if mold will spread out
            if random.choice([True, False]) is True:
                print()
#               Recursively calling itself
                self.eating(foodSource)
        else:
            print(" There is no more apples for {}  :(( ".format(self.getName()))




    def appleSearch(self, foodSource):
        '''  BOOLEAN FUNCTION: TAKE ONE PARAMETER, INSTANCE OF GIVEN OBJECT. RETURN TRUE OR FALSE '''
#       this function was created to override functionality from function searchForApple()
        print("{} is searching for an apple".format(self.getName()))
        return foodSource.searchForApple()




    def getName(self):
        ''' GETTER: RETURN OBJECT.NAME '''

        return self.name