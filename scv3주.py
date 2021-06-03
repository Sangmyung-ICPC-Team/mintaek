n = int(input())

str_list = []
for _ in range(n):
    x = str(input())
    x_cnt = len(x)
    str_list.append((x,x_cnt))
str_list = list(set(str_list))
str_list.sort(key = lambda x: (x[1], x[0]))
for x in str_list :
    print(x[0])
