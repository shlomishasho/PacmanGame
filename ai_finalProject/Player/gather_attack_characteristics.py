
from ai_finalProject.Player.common_characteristics import find_target_room,clean_and_stepforward,a_star_wrapper,get_enemy_location,euclidean_distance,enemy_in_my_room
from ai_finalProject.Search.search_methods import a_star

BASE_SHOT = 100


def attack_loc(room):
    return (room.id, room.center)


def do_attack(player,maze):

    if player.counter_attacks == 0:
        player.counter_attacks = 10
        player.calculate_play_mode(player,maze)
    else:
        clean_and_stepforward(player, maze)

    if enemy_in_my_room(player,maze):
        distance_from_enemy = euclidean_distance(player.current_loc, player.enemy.current_loc)
        print ('Player ', player.id, ' Shot')
        player.counter_attacks -= 1
        player.enemy.health_points = player.enemy.health_points - BASE_SHOT//distance_from_enemy
        player.enemy.health_points = max(0,player.enemy.health_points)
        print ('Player ', player.enemy.id, ' health points : ', player.enemy.health_points)


def init_attack_mode(player,maze):
    player.enemy = get_enemy_location(player, maze.players)
    (room_id_target, target) = find_target_room(player.enemy.current_loc, maze.rooms, attack_loc())
    player.path = a_star(maze.maze_matrix, player, target)
    a_star_wrapper(player.path, len(player.path))
    clean_and_stepforward(player,maze)