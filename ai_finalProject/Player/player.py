from math import sqrt
from random import randint
from ai_finalProject.Player.common_characteristics import *
from ai_finalProject.Player.gather_ammo_characteristics import *
from ai_finalProject.Player.gather_health_characteristics import *
from ai_finalProject.Player.gather_attack_characteristics import *
from ai_finalProject.Player.gather_defence_characteristics import *
from ai_finalProject.point import RoomPoint, PointStatus


class Player ():
    START_HEALTH_POINTS = 100
    START_AMMO_POINTS = 100
    RISK_HEALTH = 20
    LOW_AMMO = 10
    player_characteristics_options = {
        'health': [do_health, init_health_mode],
        'ammo': [do_ammo, init_ammo_mode]
        # 'defence': [do_defence, init_defence_mode],
        # 'attack': [do_attack, init_attack_mode]
    }

    def __init__(self, start_point, color):
        self._current_loc = start_point
        """have to change that"""
        self._play_mode = None
        self.func_list = [do_health, do_ammo]
        self._health_points = self.START_HEALTH_POINTS
        self._ammo_points = self.START_AMMO_POINTS
        self._color = color
        self.size = (8, 8)
        self.counter = 5
        self._path = ['TARGET', '-']
        self.enemy = None

    @property
    def path(self):
        return self._path

    @property
    def current_loc(self):
        return self._current_loc

    @current_loc.setter
    def current_loc(self, new_location):
        self._current_loc = new_location

    def step(self, maze):
        return self._play_mode (self, maze)

    def set_play_mode(self, play_mode, maze):
        print ('change play mode : ', play_mode)
        self._play_mode = self.player_characteristics_options[play_mode][0]
        self.player_characteristics_options[play_mode][1] (self, maze)

    def calculate_play_mode(self, maze):
        if enemy_in_my_room (self, maze):
            self.set_play_mode ('attack', maze)
        elif self.health_points < self.RISK_HEALTH:
            self.set_play_mode ('health', maze)
        elif self.ammo_points < self.LOW_AMMO:
            self.set_play_mode ('ammo', maze)
        else:
            if self.enough_extras ():
                self.set_play_mode ('attack', maze)
            else:
                self.set_play_mode ('defense', maze)

    def enough_extras(self):
        return self.health_points > self.START_HEALTH_POINTS / 2 and self.ammo_points > self.START_AMMO_POINTS

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

    @path.setter
    def path(self, new_path):
        self._path = new_path

    @property
    def color(self):
        return self._color

    def calculate_distance(self, other):
        return sqrt (pow (self.current_loc.x - other.x, 2) + pow (self.current_loc.y - other.y, 2))

    def evaluate_attack(self, other):

        distance = self.calculate_distance (other.current_loc)
        if self.play_mode - - other.play_mode:
            self.health_points -= (distance * 2)
            other.health_points -= (distance * 2)
        elif self.play_mode == 'attack':
            other.health_points -= (distance * 3)
        elif other.play_mode == 'attack':
            self.health_points -= (distance * 3)

        """call to function that check if one of the players health points is less or equal to zero
        ----> finish the game """

    def move(self, maze, new_location):
        maze.maze.update_player (self)
        self._current_loc = new_location
        maze.maze.update_player (self, self.color)

    @staticmethod
    def get_start_positions_for_players(number_of_rooms, number_of_players):
        setteled_players = 0
        locations = []
        while setteled_players < number_of_players:
            new_location = randint (0, number_of_rooms - 1)
            if new_location not in locations:
                setteled_players += 1
                locations.append (new_location)

        return locations

    @staticmethod
    def generate_color_for_player(player_number):
        colors = PointStatus.get_colors ()
        return colors[player_number]

    def get_room_id(self, maze):
        if not isinstance (maze[self.current_loc.x][self.current_loc.y], RoomPoint):
            return None
        else:
            return maze[self.current_loc.x][self.current_loc.y].room_id
