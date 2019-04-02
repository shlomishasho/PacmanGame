import heapq


class PriorityQueue:

    def _init(self):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _push(self, item, heappush=heapq.heappush):
        heappush(self.queue, item)

    def _pop(self, heappop=heapq.nsmallest):
        # nsmallest
        # heappop
        return heappop(self.queue)
        # return heappop(1,self.queue,key= lambda node : node.f)
    # nsmalles