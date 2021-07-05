import sys
from collections import deque
n = int(sys.stdin.readline())
queue= deque([])
for i in range(n):
    queue.append(i+1)
s = int(1)
while len(queue) > 1:
    if not s%2 == 0:
        queue.popleft()
    else:
        queue.append(queue[0])
        queue.popleft()
    s = s+1
print(queue[0])
