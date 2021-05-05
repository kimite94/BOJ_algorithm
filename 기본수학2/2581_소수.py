a = 64
b = 65
sum1 = 0
a_list = []
for i in range(a,b+1):
    sum2 = 0
    if i == 1:
        continue
    for j in range(2, i + 1):
        if i % j == 0:
            sum2 += 1
    if sum2 ==1:
        sum1 += i
        a_list.append(i)
if sum1 ==0:
    print(-1)
else:
    print(sum1)
    print(min(a_list))
