class Point():

    def __init__(self,x,y,room_id=-1):
        self._x = x
        self._y = y
        self.room_id = room_id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y