import heapq
queue = [1, 2, 3, 5, 1, 5, 8, 9, 6]
heapq.heapify(queue)  # init
heapq.heappop(queue)  # dequeue
heapq.heappush(queue, 1)  # enqueue
print(queue)
