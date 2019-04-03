from ai_finalProject.point import RoomPoint,RoomStatus
from ai_finalProject.Search.node import *
from heapq import *


def a_star(maze, player, goal):
    start = player.current_loc
    target = RoomPoint(goal[0], goal[1])
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [(start.x, start.y)]
    path = []

    new_node = Node(start, target)
    queue = []
    heappush(queue, new_node)

    while queue:
        temp_node = heappop(queue)
        current_point = temp_node.get_point()
        path.insert(len(path), current_point)
        if current_point == target:
            # path.insert(len(path), 'TARGET')
            return path
        else:
            for i, j in neighbors:
                if maze[current_point.x + i][current_point.y + j].status != RoomStatus.WALL:
                    new_node = Node(maze[current_point.x + i][current_point.y + j], target)
                    if ((current_point.x + i), (current_point.y + j)) not in visited:
                        visited.append((current_point.x + i, current_point.y + j))
                        heappush(queue, new_node)

    print('queue is empty')