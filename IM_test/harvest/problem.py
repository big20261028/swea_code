### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [ list(map(int, input())) for _ in range(n)]

    x,y = (n//2),(n//2)
    #print(x,y)

    # for row in matrix:
    #     print(row)

    benefit = 0
    for i in range(n):
        for j in range(n):
            #print(i,j)
            # # x,y에서 n보다 떨어지면 안됨
            if abs(x-i) + abs(y-j) <= n//2:
                #print(i,j)
                benefit += matrix[i][j]

    result = benefit
    print(f"#{test_case} {result}")
