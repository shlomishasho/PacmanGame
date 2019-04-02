from math import sqrt
from random import randint


class Player():
    START_HEALTH_POINTS = 10
    START_AMMO_POINTS = 6

    def __init__(self, start_point, color):
        self._current_loc = start_point
        self._play_mode = ['attack', 'health', 'ammo', 'defense']
        self._health_points = self.START_HEALTH_POINTS
        self._ammo_points = self.START_AMMO_POINTS
        self._color = color
        pass

    @property
    def current_loc(self):
        return self._current_loc

    @current_loc.setter
    def current_loc(self, new_location):
        self._current_loc = new_location

    @property
    def play_mode(self):
        return self._play_mode

    @play_mode.setter
    def play_mode(self, new_play_mode):
        self._play_mode = new_play_mode

    @property
    def health_points(self):
        return self._health_points

    @health_points.setter
    def health_points(self, new_health_status):
        self._health_points = new_health_status

    @property
    def ammo_points(self):
        return self._ammo_points

    @ammo_points.setter
    def ammo_points(self, new_ammo_status):
        self._ammo_points = new_ammo_status

    @property
    def color(self):
        return self._color

    def calculate_distance(self, other):
        return sqrt(pow(self.current_loc.x - other.x, 2) + pow(self.current_loc.y - other.y, 2))

    def evaluate_attack(self, other):

        distance = self.calculate_distance(other.current_loc)
        if self.play_mode - - other.play_mode:
            self.health_points -= (distance * 2)
            other.health_points -= (distance * 2)
        elif self.play_mode == 'attack':
            other.health_points -= (distance * 3)
        elif other.play_mode == 'attack':
            self.health_points -= (distance * 3)

        """call to function that check if one of the players health points is less or equal to zero
        ----> finish the game """

    @staticmethod
    def get_start_positions_for_players(number_of_rooms, number_of_players):
        setteled_players = 0
        locations = []
        while setteled_players < number_of_players:
            new_location = randint(0, number_of_rooms-1)
            if new_location not in locations:
                setteled_players += 1
                locations.append(new_location)

        return locations

    @staticmethod
    def generate_color_for_player(player_number):
        return (randint(player_number, 255 - player_number),) * 3
