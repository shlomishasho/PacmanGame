from math import sqrt
from random import randint
from ai_finalProject.Player.modes_util import calculate_route,euclidean_distance,check_condition,poststep


class Player():
    START_HEALTH_POINTS = 100
    START_AMMO_POINTS = 100

    def __init__(self, start_point, color):
        self._current_loc = start_point
        """have to change that"""
        self._play_mode = 'health'
        self._health_points = self.START_HEALTH_POINTS
        self._ammo_points = self.START_AMMO_POINTS
        self._color = color
        self.size = (8, 8)
        self.counter = 5
        self._path = [None]
        pass

    @property
    def path(self):
        return self._path

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

    @path.setter
    def path(self, new_path):
        self._path = new_path

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

    def move(self, maze, new_location):
        maze.update_player(self)
        self.current_loc = new_location
        maze.update_player(self, self.color)

    @staticmethod
    def get_start_positions_for_players(number_of_rooms, number_of_players):
        setteled_players = 0
        locations = []
        while setteled_players < number_of_players:
            new_location = randint(0, number_of_rooms - 1)
            if new_location not in locations:
                setteled_players += 1
                locations.append(new_location)

        return locations

    @staticmethod
    def generate_color_for_player(player_number):
        return (randint(player_number, 255 - player_number),) * 3

    def step(self,maze,rooms):
            if check_condition(self):
                poststep(self, maze)
                self._path = []
                self._path = calculate_route(self,maze,rooms)
                self.counter = 5

            self.do_step(maze)
            print(self.current_loc.x)


    def do_step(self,maze):
        # for point in self.path:
        #     yield point
        self.move(maze, self.path[0])
        del self.path[0]
        pass

    def get_most_close_room(self, rooms):
        rooms_distance = {}
        distance = 0
        for room in rooms:
            distance = euclidean_distance(room.center, self.current_loc)
            rooms_distance[room.id] = distance

        sorted_rooms_by_distance = sorted(rooms_distance.items(), key=lambda kv: kv[1])

        for id, dis in sorted_rooms_by_distance:
            if len(rooms[id].health) > 0:
                return id

        return -1
