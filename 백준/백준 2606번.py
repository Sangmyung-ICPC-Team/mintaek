n = int(input())
m = int(input())
save = [[]*n for _ in range(n+1)]
cnt = 0
for i in range(m):
    a, b = map(int,input().split())
    save[a].append(b)
    save[b].append(a)
save1 = [0] * (n+1)
def dfs(st):
    global cnt
    save1[st] = 1
    for i in save[st]:
        if save1[i]==0:
            dfs(i)
            cnt += 1
dfs(1)
print(cnt)
