### 제출 전에 지우기 ###
import sys
sys.stdin = open("input1.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    matrix = [ list(map(int, input().split())) for _ in range(n)]

    #print(matrix)
    dxy = [ (0,1), (0,-1), (1,0), (-1,0) ]

    max_num = 0

    for i in range(n):
        for j in range(m):
            total = matrix[i][j]
            for dx,dy in dxy:
                nx = i + dx
                ny = j + dy

                #if not (0 <= nx < n and 0 <= ny < m):
                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    continue

                total += matrix[nx][ny]

                # if matrix[nx][ny] > matrix[i][j]:
                #     total += matrix[i][j]
                # else:
                #     total += matrix[nx][ny]
            if total > max_num:
                max_num = total
            #print(i,j,total)

    result = max_num
    print(f"#{test_case} {result}")
