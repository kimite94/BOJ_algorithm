n = int(input())

t = [0 for i in range(n+1)]

for i in range(1,n+1):
    if i==1:
        t[i] = 0
    else:
        t[i] = t[i-1]+1
        if i%3 ==0:
            t[i] = min(t[i],t[i//3]+1)
        if i%2 ==0:
            t[i] = min(t[i],t[i//2]+1)

print(t[n])