from math import sqrt


class Node:

    def __init__(self,cur_point,target_point,g=0):
        self.cur_point = cur_point
        self.target = target_point
        self.g = g
        self.h = self.h_distance()
        self.f_value = self.f()

    def get_point(self):
        return self.cur_point

    def f(self):
        return self.g + self.h

    def h_distance(self):
        return sqrt(pow(self.cur_point.x - self.target.x, 2) + pow(self.cur_point.y - self.target.y, 2))

    def __lt__(self, other):
        if not isinstance(other,str):
            return self.f_value < other.f_value
        return False