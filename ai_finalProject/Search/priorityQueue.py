import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def qsize(self):
        return len(self.queue)

    def push(self, item, heappush=heapq.heappush):
        heappush(self.queue, item)

    def pop(self, heappop=heapq.nsmallest):
        # nsmallest
        # heappop
        return heappop(self.queue)
        # return heappop(1,self.queue,key= lambda node : node.f)
    # nsmalles