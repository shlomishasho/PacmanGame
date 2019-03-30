from math import sqrt


class Node:

    def __init__(self,start_point,target_point,g=0):
        self.start = start_point
        self.target = target_point
        self.g = g
        self.h = self.h_distance()

    def f(self):
        return self.g + self.h

    def h_distance(self):
        return sqrt(pow(self.start.x - self.target.x, 2) + pow(self.start.y - self.target.y, 2))