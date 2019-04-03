from ai_finalProject.Player.common_characteristics import find_target_room, clean_and_stepforward, a_star_wrapper, \
    euclidean_distance, get_enemy_location
from ai_finalProject.Search.search_methods import a_star

LIM_DISTANCE = 300


def defence_loc(room):
    return (room.id, room)


def do_defence(player, maze):
    if isinstance (player.path[1], str):
        print ('Player ', player.id, ' Reach to defence target : ')
        distance_from_enemy = euclidean_distance (player.current_loc, player.enemy.current_loc)
        init_defence_mode (player, maze) if distance_from_enemy < LIM_DISTANCE else player.calculate_play_mode (maze)
    else:
        clean_and_stepforward (player, maze)


def init_defence_mode(player, maze):
    player.enemy = get_enemy_location (player, maze.players)
    (room_id_target, target) = find_target_room (player.enemy.current_loc, maze.rooms, defence_loc, True)
    player.path = a_star (maze.maze.maze_matrix, player, target.center.get_location_as_tuple(), (target.width, target.height))
    a_star_wrapper (player.path, len (player.path))
    clean_and_stepforward (player, maze)
