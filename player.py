from math import sqrt

class Player():

    START_HEALTH_POINTS = 10
    START_AMMO_POINTS = 6

    def __init__(self,start_point,color):
        self._current_loc = start_point
        self._play_mode = ['attack','health','ammo']
        self._health_points = self.START_HEALTH_POINTS
        self._ammo_points = self.START_AMMO_POINTS
        self._color = color
        pass

    @property
    def current_loc(self):
        return self._current_loc

    @property
    def play_mode(self):
        return self._play_mode

    @property
    def health_points(self):
        return self._health_points

    @property
    def ammo_points(self):
        return self._ammo_points

    @property
    def color(self):
        return self._color

    def calculate_distance(self,other):
        return sqrt(pow(self.current_loc.x - other.x, 2) + pow(self.current_loc.y - other.y, 2))

    def avaluate_attak(self,other):

        distance = self.calculate_distance(other.current_loc)
        if self.play_mode -- other.play_mode :
            self.health_points -= (distance*2)
            other.health_points -= (distance*2)
        elif self.play_mode == 'attack':
            other.health_points -= (distance*3)
        elif other.play_mode == 'attack':
            self.health_points -= (distance * 3)

        """call to function that check if one of the players health points is less or equal to zero
        ----> finish the game """



