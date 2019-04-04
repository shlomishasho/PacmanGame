from ai_finalProject.Player.common_characteristics import find_target_room, clean_and_stepforward, a_star_wrapper, \
    get_enemy_location, euclidean_distance, enemy_in_my_room
from ai_finalProject.Search.search_methods import a_star

BASE_SHOT = 20


def attack_loc(room):
    return room.id, room


def do_attack(player, maze):
    in_fight=False
    if player.counter_attacks == 0:
        player.counter_attacks = player.DEFAULT_COUNTER_ATTACK
        if player.enemy.get_play_mode_id() == 2:
            return maze.reboot()
        else:
            return player.calculate_play_mode (maze)
    else:
        if enemy_in_my_room (player, maze):
            distance_from_enemy = euclidean_distance (player.current_loc, player.enemy.current_loc)
            if player.ammo_points == 0 :
                return player.set_play_mode(1,maze)
            print ('Player ', player.id, ' Shot')
            player.deacrese_trait('ammo',BASE_SHOT//3)
            player.enemy.deacrese_trait('health',BASE_SHOT // distance_from_enemy + BASE_SHOT)
            in_fight=True

        player.counter_attacks-=1

        if not isinstance(player.path[0],str):
            player.check_for_addons(maze)
            clean_and_stepforward (player, maze)
        elif not in_fight:
            return player.calculate_play_mode(maze)


def init_attack_mode(player, maze):
    player.enemy = get_enemy_location (player, maze.players)
    (room_id_target, target) = find_target_room (player.enemy.current_loc, maze.rooms, attack_loc)
    player.path = a_star (maze.maze.maze_matrix, player, target.center.get_location_as_tuple (),
                          (target.width, target.height))
    a_star_wrapper (player.path, len (player.path))
    clean_and_stepforward (player, maze)
