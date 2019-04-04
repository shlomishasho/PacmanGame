import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def qsize(self):
        return len(self.queue)

    def push(self, item, heappush=heapq.heappush):
        heappush(self.queue, item)

    def pop_value(self):
        return heapq.heappop(self.queue)
