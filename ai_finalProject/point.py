class PointStatus():
    """TODO: need to initiialize by number of players"""
    WALL = (0, 0, 0)
    SPACE = (255, 255, 255)
    PLAYER = ('some colors for Player')

    @classmethod
    def get_colors(cls):
        return [cls.WALL, cls.SPACE, cls.PLAYER]


class RoomStatus():
    HEALTH = (220, 20, 60)
    AMMO = (72, 61, 139)
    NONE = (255, 255, 255)

    @classmethod
    def get_colors(cls):
        return [cls.HEALTH, cls.AMMO, cls.NONE]


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
    def __init__(self, x, y, room_id=None, status_in_room=RoomStatus.NONE):
        super().__init__(x, y, PointStatus.SPACE)
        self._status_in_room = status_in_room
        self._room_id = room_id

    @property
    def status_in_room(self):
        return self._status_in_room

    @status_in_room.setter
    def status_in_room(self, new_status):
        self._status_in_room = new_status

    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, new_id):
        self._room_id = new_id

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
