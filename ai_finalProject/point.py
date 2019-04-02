class PointStatus():
    """TODO: need to initiialize by number of players"""
    WALL = (0, 0, 0)
    SPACE = (255, 255, 255)
    PLAYERS = [(10, 10, 10),(50,50,50)]


    @classmethod
    def get_colors(cls):
        return [cls.WALL, cls.SPACE, *cls.PLAYERS]


class RoomStatus(PointStatus):
    HEALTH = (220, 20, 60)
    AMMO = (72, 61, 139)

    @classmethod
    def get_colors(cls):
        point_color_list = super().get_colors()
        point_color_list.extend([cls.HEALTH, cls.AMMO])
        return point_color_list


class Point:

    def __init__(self, x, y, status=PointStatus.WALL):
        self._x = x
        self._y = y
        self._status = status

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        self._status = new_status


class RoomPoint(Point):
    def __init__(self, x, y, room_id=None, status=PointStatus.SPACE):
        super().__init__(x, y, status)
        self._room_id = room_id

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, new_id):
        self._room_id = new_id

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
