import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    st = sys.stdin.readline().split()

    if st[0]=='push':
        stack.append(st[1])
    elif st[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif st[0] == 'size':
        print(len(stack))
    elif st[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif st[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
