import sys
from collections import deque
n = int(sys.stdin.readline())

queue= deque([])
for i in range(n):
    qu = sys.stdin.readline().split()

    if qu[0]=='push':
        queue.append(qu[1])
    elif qu[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif qu[0] == 'size':
        print(len(queue))
    elif qu[0] == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif qu[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    elif qu[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
