import sys
k = int(sys.stdin.readline())
s = int(0)
stack=[]
for i in range(k):
    st = sys.stdin.readline().split()
    stack.append(st[0])
    if not st[0] == '0':
        s += int(stack[-1])
    else:
        stack.pop()
        s -= int(stack[-1])
        stack.pop()
print(s)
