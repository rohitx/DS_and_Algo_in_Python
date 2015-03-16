'''
R-2.4: Write a Python class, Flower, that has three instance variables of type
str, int, and float, that respectively represent the name of the flower, its
number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class
should include methods for setting the value of each type, and retrieving the
value of each type.

#Pseudo-code
Let's make UML diagram for this problem first:

------------------------------
|Class:     Flower           |
------------------------------
|Fields:  _flowerName        |
|         _petalNumber       |
|         _price             |
------------------------------
|Methods: get_flowerName()   |
|         set_flowerName()   |
|         get_petalNumber()  |
|         set_petal_Number   |
|         get_price()        |
|         set_price()        |
------------------------------

Here's how you would call the class:

import R2_4 as flower

myFlower = flower.Flower("Lily", 5, 2.05)

'''


class Flower:
    '''A flower database'''

    def __init__(self, flowerName, petalNumber, price):
        '''Create a new flower instance
        flowerName   the name of the flower
        petalNumber  the number of petals on the flower
        price        the price of the flower

        '''

        self._flowerName = flowerName
        self._petalNumber = petalNumber
        self._price = price

    def get_flowerName(self):
        '''Returns the name of the flower'''
        return self._flowerName

    def get_petalNumber(self):
        '''Returns the number of petals'''
        return self._petalNumber

    def get_price(self):
        ''' Returns price of the flower'''
        return self._price

    def set_flowerName(self, name):
        '''Sets flower Name'''
        self._flowerName = name

    def set_petalNumber(self, number):
        '''Sets the number of petals'''
        self._petalNumber = number

    def set_price(self, price):
        '''Sets the price of the flower'''
        self._price = price
