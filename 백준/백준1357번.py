x, y, w, s=map(int, input().split())
x, y=  min(x,y), max(x,y)
m = (x+y)%2
print(min((x+y)*w,x*s+(y-x)*w,(y-m)*s+m*w))

