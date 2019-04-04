import itertools
from random import randint
from ai_finalProject.Player.gather_ammo_characteristics import *
from ai_finalProject.Player.gather_health_characteristics import *
from ai_finalProject.Player.gather_attack_characteristics import *
from ai_finalProject.Player.gather_defence_characteristics import *
from ai_finalProject.Room.room import Coordinates
from ai_finalProject.point import RoomPoint, PointStatus


class Player ():
    newid = itertools.count ()

    START_HEALTH_POINTS = 100
    START_AMMO_POINTS = 100
    RISK_HEALTH = 20
    LOW_AMMO = 10
    DEFAULT_COUNTER_ATTACK=15

    def __init__(self, start_point, color):
        self.id = next (self.newid)
        self.size = (8, 8)
        self._coordinates=None
        self._current_loc = None
        self.current_loc=start_point
        self._play_mode = None
        self._play_mode_id = None
        self.func_list = [do_health, do_ammo]
        self._health_points = [self.START_HEALTH_POINTS]
        self._ammo_points = [self.START_AMMO_POINTS]
        self._color = color
        self.counter_attacks = 15
        self._path = ['TARGET']
        self.target = None
        self.enemy = None
        self.player_characteristics_options = {
            'health': [do_health, init_health_mode, self._health_points,],
            'ammo': [do_ammo, init_ammo_mode, self._ammo_points,],
            'attack': [do_attack, init_attack_mode],
            'defense': [do_defence, init_defence_mode],
        }

    @property
    def path(self):
        return self._path

    @property
    def current_loc(self):
        return self._current_loc

    @current_loc.setter
    def current_loc(self, new_location):
        self._current_loc = new_location
        left=self._current_loc.x-self.size[0]//2
        top=self._current_loc.y-self.size[1]//2
        bottom=self._current_loc.y+self.size[1]//2
        right=self._current_loc.x+self.size[0]//2

        self._coordinates=Coordinates(left,right,top,bottom)

    @property
    def coordinates(self):
        return self._coordinates
    def step(self, maze):
        if self.health_points <=0:
            return False
        self._play_mode (self, maze)
        return True

    def set_play_mode(self, play_mode, maze):
        self._play_mode_id = int (play_mode)
        functions = list (self.player_characteristics_options.values ())[self._play_mode_id ]
        self._play_mode = functions[0]
        print ('Player ', self.id, ' Mode : ', self.get_play_mode_name ())
        functions[1] (self, maze)

    def get_play_mode_id(self):
        return self._play_mode_id

    def get_play_mode_name(self):
        return list (self.player_characteristics_options.keys ())[self._play_mode_id]

    def calculate_play_mode(self, maze):
        keys = list (self.player_characteristics_options.keys ())
        if self.health_points < self.RISK_HEALTH:
            self.set_play_mode (keys.index ('health'), maze)
        elif self.ammo_points < self.LOW_AMMO:
            self.set_play_mode (keys.index ('ammo'), maze)
        else:
            self.set_play_mode (keys.index ('attack'), maze)

    def enough_extras(self):
        return self.health_points > (self.START_HEALTH_POINTS / 2) and self.ammo_points > (self.START_AMMO_POINTS / 2)

    @property
    def health_points(self):
        return self._health_points[0]

    @health_points.setter
    def health_points(self, new_health_status):
        self._health_points[0] = new_health_status

    @property
    def ammo_points(self):
        return self._ammo_points[0]

    @ammo_points.setter
    def ammo_points(self, new_ammo_status):
        self._ammo_points[0] = new_ammo_status

    @path.setter
    def path(self, new_path):
        self._path = new_path

    @property
    def color(self):
        return self._color

    def move(self, maze, new_location):
        maze.maze.update_player (self)
        self.current_loc = new_location
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
        colors = PointStatus.get_players_colors ()
        return colors[player_number]

    def get_room_id(self, maze):
        if not isinstance (maze[self.current_loc.x][self.current_loc.y], RoomPoint):
            return None
        else:
            return maze[self.current_loc.x][self.current_loc.y].room_id

    def add_to_trait(self, trait_name):
        print ("player {id} pick {name}".format (id=self.id, name=trait_name))
        old_value = self.player_characteristics_options[trait_name][2][0]
        self.player_characteristics_options[trait_name][2][0] = min (
            self.player_characteristics_options[trait_name][2][0] + 10, 100)
        new_value = self.player_characteristics_options[trait_name][2][0]
        message_to_print = "Player {id}  {trait_name} Points : {new_value}".format (id=self.id, trait_name=trait_name,
                                                                                    new_value=new_value) \
            if old_value != new_value else "Player {id} Maximum {trait_name}".format (id=self.id,trait_name=trait_name)
        print (message_to_print)

    def deacrese_trait(self, trait_name,value):
        self.player_characteristics_options[trait_name][2][0] = max (
            self.player_characteristics_options[trait_name][2][0] - value, 0)
        new_value = self.player_characteristics_options[trait_name][2][0]

        message_to_print = "Player {id}  {trait_name} Points : {new_value}".format (id=self.id, trait_name=trait_name,
                                                                                    new_value=new_value)
        print (message_to_print)

    def check_for_addons(self, maze):
        point = maze.maze.maze_matrix[self.current_loc.x][self.current_loc.y]
        if not isinstance (maze.maze.maze_matrix[self.current_loc.x][self.current_loc.y], RoomPoint):
            return False
        room_id = maze.maze.maze_matrix[self.current_loc.x][self.current_loc.y].room_id
        player_room = maze.get_room_by_id (room_id)
        addon_on_path, addon_name = player_room.get_addon_from_location (self.path[0].get_location_as_tuple ())
        if addon_on_path:
            self.add_to_trait (addon_name)
            maze.maze.remove_addon (addon_on_path)
            return True
