import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) #리스트 입력
a.sort() #정렬


e = 2e+9+1 #기준값
sol = [] 

i, j = 0, n-1 #두 포인터

while i < j:
    ai = a[i]
    aj = a[j]
    a0 = ai + aj
    
    if abs(a0) < e:
        e = abs(a0)
        sol = [ai,aj]
    if a0 < 0:
        i += 1
    else:
        j -= 1

print(sol[0], sol[1])