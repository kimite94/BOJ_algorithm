n = int(input())
x = [0 for i in range(301)]
y = [0 for i in range(301)]

for i in range(n):
    x[i] = int(input())

y[0] = x[0]
y[1] = x[0]+x[1]
y[2] = max(x[1]+x[2],x[2]+x[0])

for i in range(3,n):
    y[i] = max(y[i-2]+x[i],y[i-3]+x[i-1]+x[i])

print(y[n-1])


