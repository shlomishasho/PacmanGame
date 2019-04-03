from ai_finalProject.Player.common_characteristics import find_target_room,clean_and_stepforward,a_star_wrapper,get_enemy_location
from ai_finalProject.Search.search_methods import a_star


def defence_loc(room):
        save_loc = (room.id,room.center)
        return save_loc


def do_defence(player,maze,rooms):
    pass


def init_defence_mode(player,maze):

    player.enemy = get_enemy_location(player,maze.players)
    (room_id_target, target) = find_target_room(player.current_loc, maze.rooms, defence_loc,True)
    player.path = a_star(maze.maze_matrix, player, target)
    a_star_wrapper(player.path, len(player.path))
    pass