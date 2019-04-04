from ai_finalProject.Player.common_characteristics import find_target_room,clean_and_stepforward,a_star_wrapper
from ai_finalProject.Search.search_methods import a_star


def ammo_loc(room):

    if len(room.ammo) > 0:
        save_loc = (room.id,room.ammo[0])
        del room.ammo[0]
        return save_loc
    return False


def do_ammo(player,maze):

    if isinstance(player.path[1], str):
        player.add_to_trait('ammo')
        maze.maze.remove_addon (player.target)

        player.calculate_play_mode(maze)
    else:
        clean_and_stepforward(player,maze)


def init_ammo_mode(player,maze):
    (room_id_target, target) = find_target_room (player.current_loc, maze.rooms, ammo_loc)
    if not room_id_target:
        print("no ammo left")
    room_target = maze.get_room_by_id (room_id_target)
    target_size = (room_target.width, room_target.height)
    player.target = target
    if target is None:
        return player.calculate_play_mode (maze)
    player.path = a_star(maze.maze.maze_matrix, player, target.location, target_size)
    if player.path:
        a_star_wrapper (player.path, len (player.path))