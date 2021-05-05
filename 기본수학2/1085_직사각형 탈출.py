x, y, w, h = map(int, input().split())

a = h-y
b = w-x
print(min(x,y,a,b))   # x,y가 0일떄는 x,y가 최소가 될 수 있다.
