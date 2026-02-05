### 제출 전에 지우기 ###
import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")

### 제출 전에 지우기 ###
'''
생각 정리용 공간

딕셔너리로 높이 별 줄 갯수를 등록

'''
# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))

    # 딕셔너리로 변환
    box_dict = defaultdict(int)

    for item in arr:
        box_dict[item] += 1

    max_h = max(box_dict)
    min_h = min(box_dict)

    loop_cnt = 0
    while loop_cnt != N:

        box_dict[max_h] -= 1
        box_dict[max_h-1] += 1
        box_dict[min_h] -= 1
        box_dict[min_h+1] += 1

        if box_dict[max_h] == 0:
            max_h -= 1
        if box_dict[min_h] == 0:
            min_h += 1

        loop_cnt += 1

    result = max_h - min_h
    print(f"#{test_case} {result}")
    # ================================================================== #

    for T in range(1, 11):
        D = int(input())
        arr = list(map(int, input().split()))

        height = [min(arr), max(arr)]  # 최소, 최대 높이 저장

        for dump in range(D):
            arr[arr.index(height[0])] += 1
            arr[arr.index(height[1])] -= 1
            if (height[0] not in arr) or (height[1] not in arr):
                height = [min(arr), max(arr)]

        print(f"#{T} {height[1] - height[0]}")
