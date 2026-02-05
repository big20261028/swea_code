### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = arr[0]
    max_pos = 1
    min_pos = 1
    for idx,item in enumerate(arr):
        if max_num <= item:
            max_num = item
            max_pos = idx+1
        if min_num > item:
            min_num = item
            min_pos = idx+1
    #print(max_pos,min_pos)
    result = abs(min_pos - max_pos)
    print(f"#{test_case} {result}")
