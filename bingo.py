class Bingo:
    __bombo = []
    __extracted_balls = []
    __extracted_balls = []
    def __init__(self, bombo, extracted_balls, last_ball, carton_long):
        self.__bombo = bombo
        self.__extracted_balls = extracted_balls
        self.__last_ball = last_ball
        self.__carton_long = carton_long
    def set_bombo(self, bombo):
        self.__bombo = bombo
    def set_bombo(self, extracted_balls):
        self.__extracted_balls = extracted_balls
    def set_bombo(self, last_ball):
        self.__last_ball = last_ball
    def set_bombo(self, carton_long):
        self.__carton_long = carton_long
    def get_bombo(self, bombo):
        return self.__bombo
    def get_bombo(self, extracted_balls):
        return self.__extracted_balls
    def get_bombo(self, last_ball):
        return self.__last_ball
    def get_bombo(self, carton_long):
        return self.__carton_long