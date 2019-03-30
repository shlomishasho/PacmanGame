import itertools

class Room():

    newid = itertools.count()

    def __init__(self,center_point,width,height):
        self.id = next(self.newid)
        self._width = width
        self._height = height
        self._center = center_point

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def center(self):
        return self._center

    def is_overlap(self,other):
        return abs(self.center.x - other.center.x) < (self.width + other.width) / 2 + 5 and abs(self.center.y -
               other.center.y) < (self.height + other.height) / 2 + 5