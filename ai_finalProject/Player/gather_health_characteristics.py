from ai_finalProject.Player.common_characteristics import find_target_room, clean_and_stepforward, a_star_wrapper
from ai_finalProject.Search.search_methods import a_star


def health_loc(room):
    if len (room.health) > 0:
        save_loc = (room.id, room.health[0])
        del room.health[0]
        return save_loc
    return False


def do_health(player, maze):
    # if isinstance(player.path[1], str) and isinstance(player.path[0], str):
    #     """happen only in the start"""
    #     (room_id_target, target) = find_closest_room(player.current_loc, rooms, health_loc)
    #     player.path = a_star(maze.maze_matrix,player,target)
    print(player.path)
    if isinstance (player.path[0], str):
        print ('find new target')
        player.health_points = min (player.health_points + 10, 100)
        maze.maze.remove_addon ([10, 10], [player.target.location[0], player.target.location[1]])
        (room_id_target, target) = find_target_room (player.current_loc, maze.rooms, health_loc)
        if target is None:
            return player.calculate_play_mode(maze)
        room_target = maze.get_room_by_id (room_id_target)
        target_size = (room_target.width, room_target.height)
        player.path=None
        player.target=target
        player.path = a_star (maze.maze.maze_matrix, player, target.location, target_size)
        print(player.path)
        if player.path != []:
            a_star_wrapper(player.path, len (player.path))

    clean_and_stepforward (player, maze)


def init_health_mode(player, maze):
    (room_id_target, target) = find_target_room (player.current_loc, maze.rooms, health_loc)
    room_target= maze.get_room_by_id (room_id_target)
    target_size=(room_target.width,room_target.height)
    player.target=target
    player.path = a_star (maze.maze.maze_matrix, player, target.location, target_size)
    if player.path:
        a_star_wrapper (player.path, len (player.path))
        print("there is path !! ")


def find_target(player,maze):
