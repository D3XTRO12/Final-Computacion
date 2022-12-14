class Carton:
    __numbers = []
    def __init__(self, id, numbers, long):
        self.__id = id
        self.__numbers = numbers
        self.__long = long
    def set_id (self, id):
        self.__id = id
    def set_numbers (self, numbers):
        self.__numbers = numbers
    def set_long (self, long):
        self.__long = long
    def get_id(self, id):
        return self.__id
    def get_numbers(self, numbers):
        return self.__numbers
    def get_long(self, long):
        return self.__long
