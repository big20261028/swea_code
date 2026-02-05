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
    N, Q = map(int,input().split())
    box_arr = [ '0' for _ in range(N) ]
    change_range = [ tuple(map(int,input().split())) for _ in range(Q)]

    for i,item in enumerate(change_range):
        i = i + 1
        for idx in range(item[0]-1,item[1]):
            box_arr[idx] = str(i)
    #print(box_arr)
    result = " ".join(box_arr)
    print(f"#{test_case} {result}")
