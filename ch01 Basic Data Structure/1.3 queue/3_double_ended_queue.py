import collections
dq = collections.deque([1, 2, 3, 4])  # init
dq.appendleft(1)  # enqueue left
dq.append(2)  # enqueue right
dq.popleft()  # dequeue left
dq.pop()  # dequeue right
dq[0]  # peek left
dq[-1]  # peek right
