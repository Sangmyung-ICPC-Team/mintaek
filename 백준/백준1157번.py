n = input().lower()
n_list = list(set(n))

cnt = []

for i in n_list:
    count = n.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(n_list[(cnt.index(max(cnt)))].upper())
