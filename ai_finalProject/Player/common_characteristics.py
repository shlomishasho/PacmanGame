from ai_finalProject.Search.priorityQueue import *

from math import sqrt
#
# things that we have to do :
#     2. generate play mode each few time .
#     3. attack,defence functions
#     5. if we have a time - gather ammo,health functions
#     6. change the colors of the players, we dont want space color
#     7. one to 100 runs there is an execption of out of range,
#     8. change place of a_star and euclidean


def euclidean_distance(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


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

def get_enemy_location(player):
    pass

def a_star_wrapper(path,location):
    path.insert(location,'TARGET')


def clean_and_stepforward(player,maze):
    player.move(maze, player.path[0])
    del player.path[0]
