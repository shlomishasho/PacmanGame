import pygame
import numpy
from random import randint

from point import Point, RoomPoint, PointStatus, RoomStatus
from room import Room


class maze:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode ((self.height, self.width))
        self.maze_matrix = self.init_maze_matrix ()

    def init_maze_matrix(self):
        return [[Point (x, y) for y in range (self.width)] for x in range (self.height)]

    def draw_room(self, left, top, color, room):
        pygame.draw.rect (self.screen, color, pygame.Rect (left, top, room.width, room.height))
        for y in range (top, top + room.height):
            for x in range (left, left + room.width):
                self.maze_matrix[x][y] = RoomPoint (x, y, room.id)


class MazeGenerator:
    WHITE = (255, 255, 255)
    MAX_OF_ROOMS = 10

    def __init__(self, height, width):
        self.height = height
        self.width = width
        pygame.init ()
        self.maze = maze (width, height)
        self.rooms = []
        self.setup_maze ()

    def init_room(self, room_counter):

        x_coordinate = randint (0, self.width)
        y_coordinate = randint (0, self.height)
        """maybe -> change the size of the rectangles"""
        width_length = randint (50, 74)
        height_lenght = randint (50, 80)

        new_room = Room (Point (x_coordinate, y_coordinate), width_length, height_lenght)

        top = max(int (new_room.center.y - new_room.height / 2),0)
        bottom = int (new_room.center.y + new_room.height / 2)
        if bottom >= self.height:
            bottom = self.height - 1
            new_room.height = bottom - top

        left = max(int (new_room.center.x - new_room.width / 2),0)
        right = int (new_room.center.x + new_room.width / 2)
        if right >= self.width:
            right = self.width - 1
            new_room.width = right - left

        is_valid_room = True
        for i in range (room_counter):
            if self.rooms[i].is_overlap(new_room):
                print ('try another loc.')
                is_valid_room = False

        if is_valid_room:
            self.rooms.append (new_room)
            self.maze.draw_room (left, top, self.WHITE, new_room)
        return is_valid_room

    def setup_maze(self):

        """TODO: call here to init maze matrix"""
        done = False
        room_counter = 0
        while not done:
            for event in pygame.event.get ():
                if event.type == pygame.QUIT:
                    done = True
            if room_counter < self.MAX_OF_ROOMS:
                if self.init_room (room_counter):
                    room_counter += 1
                    pygame.display.flip ()
        """TODO : call to dig tunnels function"""

        pass


if __name__ == '__main__':
    m1 = MazeGenerator (600, 600)
