from collections import namedtuple

Coordinates = namedtuple('Coordinates', 'left right top bottom')


class Addon():
    def __init__(self,name, addon_type, room_id, location_cor=None):
        self.name=name
        self._type = addon_type
        self._center = location_cor
        self._width = 10
        self._height = 10
        self._room_id = room_id
        self._coordinates = None

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, new_room_id):
        self._room_id = new_room_id

    @property
    def location(self):
        return self._center

    @location.setter
    def location(self, new_loc):
        self._center = new_loc
        left = new_loc[0] - self.width // 2
        top = new_loc[1] - self.height // 2
        bottom = new_loc[1] + self.height // 2
        right = new_loc[0] + self.width // 2
        self._coordinates = Coordinates (left, right, top, bottom)

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width):
        self._width = new_width

    @height.setter
    def height(self, new_height):
        self._height = new_height



    def get_dimensions(self):
        return self._width, self._height

