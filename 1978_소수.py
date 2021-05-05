a = 4
b = [1,3,5,7]
sum1 = 0
for i in b:
    sum2 = 0
    if i ==1:
        continue
    for j in range(2,i+1):
        if i % j ==0:
            sum2 +=1
    if sum2 ==1:
        sum1 +=1
print(sum1)

