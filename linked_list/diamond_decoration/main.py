import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    string = input()
    # 가로열 : len(string) * 4 + 1
    # 세로열 : 5
    matrix = [ list('.' for _ in range(len(string)*4 + 1)) for _ in range(5) ]

    # 좌표 [2,2] 부터 시작, y가 4씩 늘어나며 len(string)만큼 반복

    pos = [2,2]

    for idx, char in enumerate(string):
        x, y = pos[0], pos[1] + idx*4
        matrix[x][y] = char

        for i in range(x-2,x+3,1):
            for j in range(y - 2, y + 3,1):
                if abs(i-x) + abs(j-y) == 2:
                    matrix[i][j] = '#'

    for row in matrix:
        print(''.join(row))

