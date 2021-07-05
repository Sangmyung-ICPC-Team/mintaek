n = int(input())
s = 0
for i in range(n+1,n**2,n+1):
    s += i
print(s)
