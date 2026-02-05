### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
def turn_matrix(n,matrix):
    new_list_1 = [''.join(map(str,list(matrix[row][col] for row in range(n - 1, -1, -1)))) for col in range(n)]
    new_list_2 = [''.join(map(str,list(new_list_1[row][col] for row in range(n - 1, -1, -1)))) for col in range(n)]
    new_list_3 = [''.join(map(str,list(new_list_2[row][col] for row in range(n - 1, -1, -1)))) for col in range(n)]
    return [new_list_1,new_list_2,new_list_3]

# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    result_list = turn_matrix(n,matrix)

    print(f"#{test_case}")
    for j in range(n):
        for i in range(3):
            print(result_list[i][j],end=' ')
        print()
