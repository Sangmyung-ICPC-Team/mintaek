n = int(input())
fi = []
a = 0
for i in range(n+1):
    if i == 0:
        a = 0
    elif i <= 2:
        a = 1
    else:
        a = fi[-1] + fi[-2]
    fi.append(a)

print(fi[-1])
