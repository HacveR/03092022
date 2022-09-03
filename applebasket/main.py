from appleBasket import *
from appleMold import *
from appleEater import *


basket = AppleBasket()
basket.addApples(3)
basket.addApples('QQ')

mold = AppleMold()
try:
    mold.justThrowAnError(8)
except Exception as e:
    print("\n Oops! ", e.args, " ERROR occurred. \n")

mold.eating(basket)





print(basket.getStock())