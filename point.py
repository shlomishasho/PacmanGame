from enum import Enum


class PointStatus (Enum):
    WALL = 0
    SPACE = 1
    PLAYER = 2


class RoomStatus (Enum):
    HEALTH = 3
    WEAPON = 4
    NONE=5



class Point:
    def __init__(self, x, y,status=PointStatus.WALL):
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
        self._status=new_status


class RoomPoint(Point):
    def __init__(self,x,y,room_id,status_in_room=RoomStatus.NONE):
        super().__init__(x,y,PointStatus.SPACE)
        self._status_in_room=status_in_room
        self._room_id=room_id

    @property
    def status_in_room(self):
        return self._status

    @status_in_room.setter
    def status_in_room(self, new_status):
        self._status_in_room=new_status
