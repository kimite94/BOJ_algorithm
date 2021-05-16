n = int(input())
num = list(map(int, input().split()))
operation = list(map(int, input().split()))
min_ans = 1000000000
max_ans = -1000000000
def dfs(x,y):
    global min_ans
    global max_ans
    if x == n-1:
        if y < min_ans:
            min_ans = y
        if y > max_ans:
            max_ans = y

    for i in range(4):
        cnt = y
        if operation[i] == 0:
            continue
        else:
            if i == 0:
                y += num[x+1]
            if i ==1 :
                y -= num[x+1]
            if i == 2:
                y *= num[x+1]
            if i == 3:
                if y < 0:
                    y = abs(y) // num[x + 1] * -1
                else:
                    y //= num[x + 1]
            operation[i] -= 1
            dfs(x+1, y)
            operation[i] += 1
            y = cnt



dfs(0,num[0])
print(max_ans)
print(min_ans)
