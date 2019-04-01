class Addon():
    def __init__(self, addon_type, location_cor=None):
        self._type = addon_type
        self._loc_coordinate = location_cor
        self._width = 10
        self._height = 10

    @property
    def location(self):
        return self.location

    @location.setter
    def location(self, new_loc):
        self._loc_coordinate = new_loc

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
