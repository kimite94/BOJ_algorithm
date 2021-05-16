sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(x, y) for x in range(9) for y in range(9) if sudoku[x][y] == 0]

def check(x, y):
    a_list = [1,2,3,4,5,6,7,8,9]
    for i in range(9):                      # 행에서 빈 값 찾기
        if sudoku[x][i] in a_list:
            a_list.remove(sudoku[x][i])
        if sudoku[i][y] in a_list:
            a_list.remove(sudoku[i][y])

    x = x//3
    y = y//3
    for a in range(x*3, (x+1)*3):
        for b in range(y*3, (y+1) * 3):
            if sudoku[a][b] in a_list:
                a_list.remove(sudoku[a][b])
    return a_list

ans = False
def dfs(num):
    global ans
    if ans:
        return

    if num == len(zeros):
        for i in sudoku:
            print(*i)
        ans = True
        return

    else:
        (x,y) = zeros[num]
        checking = check(x,y)
        for j in checking:
            sudoku[x][y] = j
            dfs(num+1)
            sudoku[x][y] =0

dfs(0)





