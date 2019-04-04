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

    def get_addon_from_location(self,location):
        types=['health','ammo']
        addons=[self.ammo,self.health]
        for i in range(len(addons)):
            for addon in addons[i]:
                if location[0] in range(addon.coordinates.left,addon.coordinates.right):
                    if location[1] in range(addon.coordinates.top,addon.coordinates.bottom):
                        addons[i].remove(addon)
                    return addon,types[i]

        return None,None

    def set_room_addons(self, maze):
        ammo_amount = randint(0, 3)
        self._ammo = self._health = []
        health_amount = randint(0, 3)

        for i in range(0, ammo_amount):
            self.ammo.append(self._set_room_addon(maze,'ammo', self.AMMO))
        for i in range(0, health_amount):
            self.health.append(self._set_room_addon(maze,'health', self.HEALTH))

    def _set_room_addon(self, maze,name, color):
        while True:
            new_addon = Addon(name,color,self.id)
            x_location = randint(self.coordinates.left, self.coordinates.right)
            y_location = randint(self.coordinates.top, self.coordinates.bottom)
            new_addon.width = min(new_addon.width + x_location, self.coordinates.right) - x_location
            new_addon.height = min(y_location + new_addon.height, self.coordinates.bottom) - y_location
            if new_addon.width >1 and new_addon.height >1:
                x_center=x_location+new_addon.width//2
                y_center=y_location+new_addon.height//2
                new_addon.location = (x_center, y_center)
                maze.draw_addons(color, (new_addon.width , new_addon.height), (x_location, y_location,))
                return new_addon
