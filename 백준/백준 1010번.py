import math

a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    s = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(s)
