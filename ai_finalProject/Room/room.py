import itertools
from collections import namedtuple
from random import randint
from ai_finalProject.Room.addon import Addon

Coordinates = namedtuple('Coordinates', 'left right top bottom')


class Room:
    newid = itertools.count()
    AMMO = (72, 61, 139)
    HEALTH = (220, 20, 60)

    def __init__(self, center_point, width, height, ):
        self.id = -1
        self._width = width
        self._height = height
        self._center = center_point
        self._ammo = []
        self._health = []
        self.coordinates = None

    def set_id(self):
        self.id = next(self.newid)
    @property
    def health(self):
        return self._health

    @property
    def ammo(self):
        return self._ammo

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def center(self):
        return self._center

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @health.setter
    def health(self, new_health):
        self._health = new_health

    @ammo.setter
    def ammo(self, new_ammo):
        self._ammo = new_ammo


    def is_overlap(self, other):
        return abs(self.center.x - other.center.x) < (self.width + other.width) / 2 + 5 and abs(self.center.y -
                                                                                                other.center.y) < (
                       self.height + other.height) / 2 + 5


    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_room_addons(self, maze):
        ammo_amount = randint(0, 3)
        self._ammo = self._health = []
        health_amount = randint(0, 3)

        for i in range(0, ammo_amount):
            self.ammo.append(self._set_room_addon(maze, self.AMMO))
        for i in range(0, health_amount):
            self.health.append(self._set_room_addon(maze, self.HEALTH))

    def _set_room_addon(self, maze, color):
        new_addon = Addon(color,self.id)
        x_location = randint(self.coordinates.left, self.coordinates.right)
        y_location = randint(self.coordinates.top, self.coordinates.bottom)
        width = max(new_addon.width + x_location, self.coordinates.right) - x_location
        height = max(y_location + new_addon.height, self.coordinates.bottom) - y_location
        x_location = max(self.coordinates.left, (x_location - width))
        y_location = max(self.coordinates.top, (y_location - height))
        new_addon.location = (x_location, y_location)
        maze.draw_addons(color, (new_addon.width, new_addon.height,), (x_location, y_location,))
        return new_addon
