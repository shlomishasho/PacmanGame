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
        return sqrt(pow(self.start.x - self.target[0], 2) + pow(self.start.y - self.target[1], 2))