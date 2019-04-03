from ai_finalProject.Search.priorityQueue import *
from ai_finalProject.Search.node import *
from ai_finalProject.point import RoomPoint,RoomStatus
from heapq import *

from math import sqrt
#
# things that we have to do :
#     2. generate play mode each few time .
#     3. attack,defence functions
#     5. if we have a time - gather ammo,health functions
#     6. change the colors of the players, we dont want space color
#     7. one to 100 runs there is an execption of out of range,
#     8. change place of a_star and euclidean

def a_star(maze, player, goal):
    start = player.current_loc
    target = RoomPoint(goal[0], goal[1])
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [(start.x, start.y)]
    path = []

    new_node = Node(start, target)
    queue = []
    heappush(queue, new_node)

    while queue:
        temp_node = heappop(queue)
        current_point = temp_node.get_point()
        path.insert(len(path), current_point)
        if current_point == target:
            path.insert(len(path), 'TARGET')
            return path
        else:
            for i, j in neighbors:
                if maze[current_point.x + i][current_point.y + j].status != RoomStatus.WALL:
                    new_node = Node(maze[current_point.x + i][current_point.y + j], target)
                    if ((current_point.x + i), (current_point.y + j)) not in visited:
                        visited.append((current_point.x + i, current_point.y + j))
                        heappush(queue, new_node)

    print('queue is empty')


def euclidean_distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def health_loc(room):
    if len(room.health) > 0:
        save_loc = (room.id,room.health[0].location)
        del room.health[0]
        return save_loc
    return False


def ammo_loc(room):
    if len(room.ammo) > 0:
        save_loc = (room.id,room.ammo[0].location)
        del room.ammo[0]
        return save_loc
    return False


def find_closest_room(player_loc, rooms,f):

    id_center = list(map(lambda r:(euclidean_distance(r.center,player_loc),r.id),rooms))
    sorted_rooms = sorted(id_center,key=lambda k: k[0])
    for dis,id  in sorted_rooms:
        room = rooms[int(id)]
        loc = f(room)
        if loc:
            return loc

    print('no left health points')
    return None


def clean_and_stepforward(player,maze):
    player.move(maze, player.path[0])
    del player.path[0]


def do_health(player,maze,rooms):

    if isinstance(player.path[1], str) and isinstance(player.path[0], str):
        """happen only in the start"""
        (room_id_target, target) = find_closest_room(player.current_loc, rooms, health_loc)
        player.path = a_star(maze.maze_matrix,player,target)
    elif isinstance(player.path[1], str):
        player.health_points = min(player.health_points + 10, 100)
        maze.remove_addon([10, 10], [player.path[0].x,player.path[0].y])
        (room_id_target,target) = find_closest_room(player.current_loc,rooms,health_loc)
        player.path = a_star(maze.maze_matrix,player,target)

    clean_and_stepforward(player,maze)


def do_ammo(player,maze,rooms):

    if isinstance(player.path[1], str) and isinstance(player.path[0], str):
        """happen only in the start"""
        (room_id_target, target) = find_closest_room(player.current_loc, rooms, ammo_loc)
        player.path = a_star(maze.maze_matrix,player,target)
    elif isinstance(player.path[1], str):
        player.ammo_points = min(player.ammo_points + 10, 100)
        maze.remove_addon([10, 10], [player.path[0].x,player.path[0].y])
        (room_id_target,target) = find_closest_room(player.current_loc,rooms,ammo_loc)
        player.path = a_star(maze.maze_matrix,player,target)

    clean_and_stepforward(player,maze)

