
def check(n):
    for i in range(n):
        if row[n]==row[i] or abs(row[n]-row[i]) == n-i:
            return False
    return True


def chess(n):
    global cnt              # 변수 선언(함수 내에서도 사용할 수 있게)
    if n == N:
        cnt +=1
    else:
        for i in range(N):
            row[n] =i
            if check(n) == True:
                chess(n+1)

N = int(input())
row = [0]*N
cnt = 0
chess(0)
print(cnt)
