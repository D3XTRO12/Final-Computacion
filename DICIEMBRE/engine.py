import random
from bingo import *
from constants import carton as cart
from carton import *
user_cart_long = int(input("Select the carton Long:"))
class Engine:
    __carton = cart()
    def __init__(self) -> None:
        self.__carton = list(map(lambda x: str(x), random.choice(cart()), Carton.get_long(user_cart_long)))
        self.__origin = self.__carton.copy()
        print(self.__origin)
        self._bomboNumbers = cart

    def show_carton(self):
        carton=self._origin if origin else self._carton
        for i in range (0, len[carton], 4):
            print(carton[i:i+4])
    def get_bombo_number(self):
        numeroPos=random.choice(cart()-1)
        pick = self._bomboNumbers[numeroPos]
        del self._bomboNumbers[numeroPos]
        self._pickedNumber.append(pick)
        return pick

Engine().show_carton