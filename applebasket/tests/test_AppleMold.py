import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import pytest
from applebasket.appleMold import AppleMold



def test_appleMoldyName():
    ''' Testing initialized default object name'''
    applemold = AppleMold()
    assert  applemold.getName() == "Mr Moldy"

def test_justThrowAnError_greater():
    ''' Testing for error occurring when value is greater than 10'''
    applemold = AppleMold()
    with pytest.raises(ValueError):
        applemold.justThrowAnError(11)

def test_justThrowAnError_smaller():
    ''' Testing for error occurring when value is smaller than 11'''
    applemold = AppleMold()
    with pytest.raises(ValueError):
        applemold.justThrowAnError(10)










