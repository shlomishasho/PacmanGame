import pygame
import numpy
from random import randint

from ai_finalProject.point import Point, RoomPoint, PointStatus, RoomStatus
from ai_finalProject.Room.room import Room, Coordinates
from ai_finalProject.Player.player import Player


class maze:
    TUNNEL_WIDTH = 5

    def __init__(self, width, height):
        self.height = height
        self.width = width
        pygame.init()
        self.screen = pygame.display.set_mode((self.height, self.width))
        self.maze_matrix = self.init_maze_matrix()

    # Region functions for init the Maze
    def init_maze_matrix(self):
        return [[Point(x, y) for y in range(self.width)] for x in range(self.height)]

    def draw_addons(self, color, size, location):
        pygame.draw.rect (self.screen, color, pygame.Rect (location[0], location[1], size[0], size[1]))

    def draw_room(self, color, room):
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(room.coordinates.left, room.coordinates.top, room.width, room.height))
        for y in range(room.coordinates.top, room.coordinates.top + room.height):
            for x in range(room.coordinates.left, room.coordinates.left + room.width):
                self.maze_matrix[x][y] = RoomPoint(x, y, room.id)

    def draw_tunnel(self, src_point, target_point, color, joint_point=None):
        if not joint_point:
            self.draw_line(src_point, target_point, color, self.TUNNEL_WIDTH)
        else:
            self.draw_line(src_point, joint_point, color, self.TUNNEL_WIDTH)
            self.draw_line(joint_point, target_point, color, self.TUNNEL_WIDTH)

    def draw_line(self, src_point, target_point, color, width=2):
        pygame.draw.line(self.screen, color, (src_point.x, src_point.y), (target_point.x, target_point.y), width)

    def update_matrix_after_init(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                color = self.screen.get_at((x, y,))
                if self.is_same_color(color, (0, 0, 0,)):
                    pass
                else:
                    for game_color in PointStatus.get_colors():
                        if self.is_same_color(color, game_color):
                            self.maze_matrix[x][y].status = game_color
                        if isinstance(self.maze_matrix[x][y], RoomPoint):
                            for room_color in RoomStatus.get_colors():
                                if self.is_same_color(color, room_color):
                                    self.maze_matrix[x][y].status = color

    def is_same_color(self, color1, color2):
        for i in range(0, len(color2)):
            if color1[i] != color2[i]:
                return False
        return True

    # End Region

    def remove_addon(self, size, location):
        pygame.draw.rect(self.screen, PointStatus.SPACE, pygame.Rect(location[0], location[1], size[0], size[1]))
        self.update_element_on_matrix(location, size, RoomStatus.SPACE)

    def update_player(self, player, color=PointStatus.SPACE):
        pygame.draw.rect(self.screen, color,
                         pygame.Rect(player.current_loc.x, player.current_loc.y, *player.size))
        self.update_element_on_matrix(player.current_loc.get_location_as_tuple(), player.size, color)

    def update_element_on_matrix(self, location, size, new_status):
        for x in range(location[0], location[0] + size[0]):
            for y in range(location[1], location[1] + size[1]):
                self.maze_matrix[x][y].status = new_status


class MazeGenerator:
    WHITE = (255, 255, 255)
    MAX_OF_ROOMS = 3

    def __init__(self, height, width, number_of_players):
        self.height = height
        self.width = width
        self.maze = maze(width, height)
        self.rooms = []
        self.players = []
        self.number_of_players = number_of_players

    def init_rooms(self):
        room_counter = 0
        while room_counter < self.MAX_OF_ROOMS:
            if self.init_room(room_counter):
                room_counter += 1

    def init_room(self, room_counter):
        x_coordinate = randint(0, self.width - 1)
        y_coordinate = randint(0, self.height - 1)
        """maybe -> change the size of the rectangles"""
        width_length = randint(50, 74)
        height_lenght = randint(50, 80)

        self.maze.maze_matrix[x_coordinate][y_coordinate] = RoomPoint(x_coordinate, y_coordinate)
        new_room = Room(self.maze.maze_matrix[x_coordinate][y_coordinate], width_length, height_lenght)
        self.maze.maze_matrix[x_coordinate][y_coordinate].room_id = new_room.id

        top = max(int(new_room.center.y - new_room.height / 2), 0)
        bottom = int(new_room.center.y + new_room.height / 2)
        if bottom >= self.height:
            bottom = self.height - 1
            new_room.height = bottom - top

        left = max(int(new_room.center.x - new_room.width / 2), 0)
        right = int(new_room.center.x + new_room.width / 2)
        if right >= self.width:
            right = self.width - 1
            new_room.width = right - left

        is_valid_room = True
        for i in range (room_counter):
            if self.rooms[i].is_overlap (new_room):
                print ('is_overlap , try another loc.')
                is_valid_room = False

        new_room.set_coordinates(Coordinates(left, right, top, bottom))
        if is_valid_room:
            self.rooms.append(new_room)
            self.maze.draw_room(self.WHITE, new_room)

        return is_valid_room

    def init_tunnles(self):
        has_tunnel_connection = []
        for room_src in self.rooms:
            for room_trg in self.rooms:
                if room_src != room_trg and (room_src.id,room_trg.id) not in has_tunnel_connection:
                    has_tunnel_connection.extend(((room_src.id,room_trg.id),(room_trg.id,room_src.id)))
                    self.init_tunnel(room_src, room_trg)

    def init_tunnel(self, room_source, room_target):
        if room_source.center < room_target.center:
            return
        joint_point = None
        if room_source.center.x != room_target.center.x and room_source.center.y != room_target.center.y:
            joint_point = Point(room_source.center.x, room_target.center.y)
        self.maze.draw_tunnel(room_source.center, room_target.center, self.WHITE, joint_point)

    def init_addons(self):
        for room in self.rooms:
            room.set_room_addons(self.maze)

    def init_players(self, number_of_players):
        locations = Player.get_start_positions_for_players(len(self.rooms), number_of_players)
        for new_player_num in range(0, number_of_players):
            room_for_player = self.rooms[locations[new_player_num]]
            new_color = Player.generate_color_for_player(new_player_num)
            self.players.append(Player(room_for_player.center, new_color))
            self.maze.update_player(self.players[new_player_num])

    def start_game(self):
        done = False
        self.setup_maze()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                pygame.display.flip()

            for player in self.players:
                """here we will discuss in the order of the modes of each player, how to do it,
                for now i'm just checking the astar func"""
                player.search(self.maze,self.rooms)
                pygame.display.flip()

    def setup_maze(self, ):
        self.init_rooms()
        self.init_tunnles()
        self.init_addons()
        self.init_players(self.number_of_players)
        pygame.display.flip()

        self.maze.update_matrix_after_init()


if __name__ == '__main__':
    m = MazeGenerator(600, 600, 2)
    m.start_game()
