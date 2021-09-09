import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

x = int(input())

cnt = 0

i, j = 0, n-1

while i != j:
    if a[i] + a[j] == x:
        cnt += 1
        i += 1
    elif a[i] + a[j]>x:
        j -= 1
    else:
        i += 1

print(cnt)

