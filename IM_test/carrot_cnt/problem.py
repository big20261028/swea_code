### 제출 전에 지우기 ###
import sys
sys.stdin = open("carrot_sample_in.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    max_cnt = 0
    cnt = 1
    for idx in range(len(arr)-1):
        if arr[idx] < arr[idx+1]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

    result = max_cnt
    print(f"#{test_case} {result}")
