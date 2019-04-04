from ai_finalProject.point import RoomPoint, RoomStatus, Point, PointStatus
from ai_finalProject.Search.node import *
from heapq import *
from ai_finalProject.Search.priorityQueue import *



def a_star(maze, player, goal, goal_size):
    start = player.current_loc
    target = RoomPoint (goal[0], goal[1])
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [(start.x, start.y)]
    path = []
    new_node = Node (start, target)
    queue = PriorityQueue()
    queue.push(new_node)

    while queue:
        temp_node = queue.pop_value()
        current_point = temp_node.get_point()
        path.insert(len(path), current_point)
        if reached_to (target, goal_size, current_point):
            return path
        else:
            for i, j in neighbors:
                object_loc_x = current_point.x + int (player.size[0]) * i
                object_loc_y = current_point.y + int (player.size[0]) * j
                if (object_loc_x) >= len (maze[0]) or (object_loc_y) >= len (maze):
                    pass
                elif is_free_space (object_loc_x, object_loc_y, maze, [PointStatus.WALL],
                                    player.size):
                    new_node = Node (maze[object_loc_x][object_loc_y], target)
                    if (object_loc_x, object_loc_y) not in visited:
                        visited.append ((object_loc_x, object_loc_y))
                        queue.push(new_node)

    print ('queue is empty')



def reached_to(target, target_size, location):
    if location.x in range (target.x - target_size[0] // 2, target.x + (target_size[0] // 2)+1):
        if location.y in range (target.y - target_size[1] // 2, target.y + (target_size[1] // 2)+1):
            return True
    return False

def is_free_space(x, y, maze, colors, size):
    for i in range (x - size[0] // 2, min(x + size[0] // 2,len(maze))):
        for j in range (y - size[1] // 2, min(y + size[1] // 2,len(maze))):
            if maze[i][j].status in colors:
                return False
    return True