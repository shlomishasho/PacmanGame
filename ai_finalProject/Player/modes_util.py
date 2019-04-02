from ai_finalProject.Search.priorityQueue import *
from ai_finalProject.Search.node import *
from ai_finalProject.point import RoomPoint
from math import sqrt


def a_star(maze,player,target):
    found = False
    start = player.current_loc
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [(start.x,start.y)]

    new_node = Node(start,target)
    queue = PriorityQueue()
    queue._push(new_node)

    while queue and not found:
        temp_node = queue._pop()
        current_point = temp_node.get_point()
        player.move(current_point)
        maze.draw_player(player)
        if current_point == target:
            found = True
        else:
            for i,j in neighbors:
                new_node = Node(maze[current_point.x +i][current_point.y+j],target)
                if ((current_point.x +i),(current_point.y+j)) not in visited:
                    visited.append((current_point.x +i),(current_point.y+j))
                    queue._push(new_node)

    if not found:
        print('problem .. the queue is empty and the target didnt found')

    return found


# euclidean distance function
def euclidean_distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def attack_step(**kwargs):
    pass


def get_most_close_room(player,rooms):
    rooms_distance = {}
    distance = 0
    for room in rooms:
        distance = euclidean_distance(room.center,player.current_loc)
        rooms_distance[room.id] = distance

    sorted_rooms_by_distance = sorted(rooms_distance.items(),key=lambda kv : kv[1])

    for id,dis in sorted_rooms_by_distance:
        if len(rooms[id].health) > 0:
            return id

    return -1


def health_step(**kwargs):
    """explenation:
        - args:
            by this order - maze,start point,player
        1. get most close room id
        1. get one of the health points in the room and marked her as a target
        2. call to Astar to find the point
        3. update health points """
    closest_room = get_most_close_room(kwargs['player'],kwargs['rooms'])
    a_star(kwargs['maze'],kwargs['player'],kwargs['rooms'][closest_room].health[0].location)
    kwargs['maze'].remove_addon(([10,10],kwargs['rooms'][closest_room].health[0].location))
    del kwargs['rooms'][closest_room].health[0]
    kwargs['player'].health = min(kwargs['player'].health + 10,100)



def ammo_step(**kwargs):
    pass


def defence_step(**kwargs):
    pass


def step(player,maze,rooms):
    modes = {
        'health': health_step(player = player,maze = maze, rooms =rooms),
        'attack': attack_step(player,maze),
        'ammo': ammo_step(player,maze),
        'defence': defence_step(player,maze)
    }

    return modes[player.play_mode]