from ai_finalProject.Search.priorityQueue import *
from ai_finalProject.Search.node import *
from ai_finalProject.point import RoomPoint
from heapq import *

from math import sqrt


def a_star(maze,player,goal):

    start = player.current_loc
    target = RoomPoint(goal[0],goal[1])
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [(start.x,start.y)]
    path = []

    new_node = Node(start,target)
    queue = []
    heappush(queue,new_node)

    while queue:
        temp_node = heappop(queue)
        current_point = temp_node.get_point()
        path.insert(len(path),current_point)
        if current_point == target:
            path.insert(len(path), None)
            return path
        else:
            for i,j in neighbors:
                new_node = Node(maze[current_point.x +i][current_point.y + j],target)
                if ((current_point.x +i),(current_point.y+j)) not in visited:
                    visited.append((current_point.x +i,current_point.y+j))
                    heappush(queue,new_node)

    print('queue is empty')



# euclidean distance function
def euclidean_distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def attack_step(**kwargs):
    pass

def health_prestep(**kwargs):
    """explenation:
        - args:
            by this order - maze,start point,player
        1. get most close room id
        1. get one of the health points in the room and marked her as a target
        2. call to Astar to find the point
        """

    closest_room = kwargs['player'].get_most_close_room(kwargs['rooms'])
    path = a_star(kwargs['maze'],kwargs['player'],kwargs['rooms'][closest_room].health[0].location)
    return path


def ammo_step(**kwargs):
    pass


def defence_step(**kwargs):
    pass


def calculate_route(player,maze,rooms):
    modes = {
        'health': health_prestep(player = player,maze = maze.maze_matrix, rooms =rooms)
        # 'attack': attack_step(player,maze),
        # 'ammo': ammo_step(player,maze),
        # 'defence': defence_step(player,maze)
    }

    return modes[player.play_mode]