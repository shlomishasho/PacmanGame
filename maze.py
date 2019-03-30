import pygame
import numpy
from random import randint
import itertools

from point import  Point
from room import Room

class MazeGenerator():

    WHITE = (255, 255, 255)
    MAX_OF_ROOMS = 10

    def __init__(self,height,width):
        self.height = height
        self.width = width
        pygame.init()
        self.screen = pygame.display.set_mode((self.height, self.width))
        # self.screen = pygame.Surface((self.height, self.width))
        # check = pygame.PixelArray(self.screen)
        self.maze = numpy.empty((height,width,))
        self.maze[:] = numpy.nan

        self.rooms = []
        self.setup_maze()

    def init_room(self,room_counter):

        x_coordinate = randint(0, self.width)
        y_coordinate = randint(0, self.height)
        """maybe -> change the size of the rectangles"""
        width_length = randint(50, 74)
        height_lenght = randint(50,80)

        new_room = Room(Point(x_coordinate, y_coordinate),width_length, height_lenght)

        top = new_room.center.y - new_room.height / 2
        if top < 0:
            top = 0
        bottom = new_room.center.y + new_room.height / 2
        if bottom >= self.height:
            bottom = self.height - 1
        left = new_room.center.x - new_room.width / 2
        if left < 0:
            left = 0
        right = new_room.center.x + new_room.width / 2
        if right >= self.width:
            right = self.width - 1

        is_valid_room = True
        print(room_counter)
        for i in range(room_counter):
            if self.rooms[i].is_overlap(new_room):
                print('try another loc.')
                is_valid_room = False

        if is_valid_room:
            """TODO : enter to maze points"""
            self.rooms.append(new_room)
            pygame.draw.rect(self.screen, self.WHITE, pygame.Rect(left, top, new_room.width, new_room.height))
            # for i in range(top,bottom):
            #     for j in range(left,right):
            #         self.maze[i][j] = Point(i,j,new_room.id)
            return True
        else:
            return False

    def setup_maze(self):

        """TODO: call here to init maze matrix"""
        done = False
        room_counter = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if room_counter < self.MAX_OF_ROOMS:
                if self.init_room(room_counter):
                    room_counter += 1
                    pygame.display.flip()
        """TODO : call to dig tunnels function"""

        pass
if __name__ == '__main__':
    m1 = MazeGenerator(600,600)
