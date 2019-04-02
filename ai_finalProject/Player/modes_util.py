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

def check_condition(player):
    return player.path[0] == None if player.play_mode == 'health' or player.play_mode == 'ammo' else player.path[0] == None or player.counter == 0

def post_health_step(player,maze):
    player.health_points = min(player.health_points + 10, 100)
    maze.remove_addon([10,10],player.path[len(player.path) -1 ])

def prestep(player,maze,rooms,get_target):

    closest_room = get_target(rooms)
    return a_star(maze,player,rooms[closest_room].health[0].location)


def poststep(player,maze):
    """maybe will change like pre step that send fucntion"""
    if player.path[0] != None :
        modes = {
           'health': post_health_step(player, maze)
        }
        modes[player.play_mode]

def get_enemy_target():
    pass


def calculate_route(player,maze,rooms):
    modes = {
        'health': prestep(player,maze.maze_matrix,rooms,player.get_most_close_room)
        # 'attack':  prestep(player,maze.maze_matrix,rooms,get_enemy_target),
        # 'ammo':  prestep(player,maze.maze_matrix,rooms,get_enemy_target),
        # 'defence':  prestep(player,maze.maze_matrix, rooms,get_enemy_target)
    }

    return modes[player.play_mode]