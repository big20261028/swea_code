### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    good_home = 0
    for idx in range(2,N-2):
        L_view = max(arr[idx-1],arr[idx-2])
        R_view = max(arr[idx+1],arr[idx+2])
        total = arr[idx] - max(L_view,R_view)
        if total > 0 :
            good_home += total
            #print("good_home 갱신",good_home)


    result = good_home
    print(f"#{test_case} {result}")
