n, s = map(int,input().split())
a = list(map(int, input().split())) #리스트 입력

sum_a = [0] * (n+1)
for b in range(1,n+1):
    sum_a[b] = sum_a[b-1] + a[b-1]

i, j = 0, 1
e = 1000001

while i != n:
    if sum_a[j] - sum_a[i] >= s:
        if j - i < e:
            e = j - i
        i += 1
    else:
        if j != n:
            j += 1
        else:
            i += 1
if e != 1000001:
    print(e)
else:
    print(0)