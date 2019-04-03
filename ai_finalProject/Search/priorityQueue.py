import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def qsize(self):
        return len(self.queue)

    def push(self, item, heappush=heapq.heappush):
        heappush(self.queue, item)

    # def pop_val(self):
    #     return heapq.heappop(self.queue)

    def pop_value(self):
        # nsmallest
        # heappop
        return heapq.heappop(self.queue)
        # return heappop(1,self.queue,key= lambda node : node.f)
    # nsmalles