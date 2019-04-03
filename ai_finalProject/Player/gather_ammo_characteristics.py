from ai_finalProject.Player.common_characteristics import find_closest_room,clean_and_stepforward
from ai_finalProject.Search.search_methods import a_star

def do_ammo(player,maze,rooms):

    # if isinstance(player.path[1], str) and isinstance(player.path[0], str):
    #     """happen only in the start"""
    #     (room_id_target, target) = find_closest_room(player.current_loc, rooms, ammo_loc)
    #     player.path = a_star(maze.maze_matrix,player,target)
    if isinstance(player.path[1], str):
        player.ammo_points = min(player.ammo_points + 10, 100)
        maze.remove_addon([10, 10], [player.path[0].x,player.path[0].y])
        (room_id_target,target) = find_closest_room(player.current_loc,rooms,ammo_loc)
        player.path = a_star(maze.maze_matrix,player,target)

    clean_and_stepforward(player,maze)

def ammo_loc(room):
    if len(room.ammo) > 0:
        save_loc = (room.id,room.ammo[0].location)
        del room.ammo[0]
        return save_loc
    return False

def init_ammo_mode(player,maze,rooms):
    pass