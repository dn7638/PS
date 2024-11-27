# 보드
# 1,1 말
# 새로이동한 칸 -> 지금까지 알파벳과 달라야함
import sys

input = sys.stdin.readline

R, C = map(int, input().split(' '))
board = [list(input()) for _ in range(R)]

alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
         'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
         'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
         'W': 0, 'X': 0, 'Y': 0, 'Z': 0, }
alpha[board[0][0]] += 1
plusX=[-1,1,0,0]
plusY=[0,0,-1,1]

answer = [1]


def btk(x, y, cnt):
    if cnt > answer[0]:
        answer[0] = cnt
        if answer[0] == 26:
            print(answer[0])
            exit()

    for i in range(4):
        n_x = x + plusX[i]
        n_y = y + plusY[i]

        if 0 <= n_x < R and 0 <= n_y < C and alpha[board[n_x][n_y]] == 0:
        
            alpha[board[n_x][n_y]] = 1
            btk(n_x, n_y, cnt + 1)
            alpha[board[n_x][n_y]] = 0


btk(0, 0, 1)

print(answer[0])
