### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간

'''
# 테스트 케이스
for test_case in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_val = 0
    for row in arr:
        if sum(row) > max_val:
            max_val = sum(row)

    col_list = []
    for i in range(100):
        col_list.append([ row[i] for row in arr ])
    for col in col_list:
        if sum(col) > max_val:
            max_val = sum(col)
    #print(len(col_list))

    sum_data = 0
    for i in range(100):
        sum_data += arr[i][i]
    if sum_data > max_val:
        max_val = sum_data

    sum_data = 0
    for i in range(100):
        sum_data += arr[i][len(arr)-1-i]
    if sum_data > max_val:
        max_val = sum_data

    result = max_val
    print(f"#{test_case} {result}")
