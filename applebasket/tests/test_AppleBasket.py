from applebasket.appleBasket import AppleBasket


def test_applebasket_Defoult():
    ''' Testing if object is initialized with stock  0 '''
    applebasket = AppleBasket()
    assert applebasket.getStock() == 0

def test_positive_searchForApple():
    ''' Testing if f. return TRUE for stock > 0 '''
    applebasket = AppleBasket()
    applebasket.addApple()
    assert applebasket.searchForApple() is True

def test_negative_searchForApple():
    ''' Testing if f. return FALSE for stock < 1'''
    applebasket = AppleBasket()
    assert applebasket.searchForApple() is False

def test_addApple():
    ''' Testing if value is incremented by 1 '''
    applebasket = AppleBasket()
    applebasket.addApple()
    assert  applebasket.getStock() == 1

def test_takeApple():
    ''' Testing if value is reduced by 1 '''
    applebasket = AppleBasket()
    applebasket.addApple()
    applebasket.takeApple()
    assert applebasket.getStock() == 0

def test_negativeStock():
    ''' Testing for negative value in the stock '''
    applebasket = AppleBasket()
    applebasket.takeApple()
    assert applebasket.getStock() == 0

def test_Non_Integer_addApples():
    ''' Testing if NOT INTEGER is given'''
    applebasket = AppleBasket()
    applebasket.addApples('Ten')
    assert applebasket.getStock() == 0

def test_negative_addApples():
    ''' Testing if negative value is given'''
    applebasket = AppleBasket()
    applebasket.addApples(-10)
    assert applebasket.getStock() == 0

def test_addApples():
    ''' Testing if addApples for correct amount'''
    applebasket = AppleBasket()
    applebasket.addApples(10)
    assert  applebasket.getStock() == 10

def test_Non_Integer_takeApples():
    ''' Testing if NOT INTEGER is given'''
    applebasket = AppleBasket()
    applebasket.takeApples('Eight')
    assert applebasket.getStock() == 0

def test_negative_takeApples():
    ''' Testing if negative value is given'''
    applebasket = AppleBasket()
    applebasket.takeApples(-10)
    assert applebasket.getStock() == 0

def test_amount_greater_than_stock_TakeApples():
    ''' Test if number is greater than stock '''
    applebasket = AppleBasket()
    applebasket.addApple()
    applebasket.takeApples(2)
    assert applebasket.getStock() == 0

