n = int(input())
cnt = 0
n6 = 666
while True:
    if '666' in str(n6):
        cnt += 1
    if cnt == n:
        print(n6)
        break
    n6 += 1
