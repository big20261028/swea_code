### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
def stop_count(k,n,stop_dict):
    start_point = 0
    cnt = 0
    while start_point < n:
        start_point += k
        if start_point >= n:
            break
        loop_cnt = 0
        while stop_dict[start_point] == 'X':
            start_point -= 1
            loop_cnt += 1
            if loop_cnt == k:
                return 0
        if stop_dict[start_point] == 'O':
            cnt += 1
    return cnt


# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    k,n,m = map(int,input().split())
    arr = list(map(int, input().split()))

    stop_list = [ i for i in range(n+1) ]
    charge_list = [i for i in range(1, n + 1) if i in arr ]
    stop_dict = { i:('O' if i in charge_list else 'X') for i in stop_list }

    result = stop_count(k,n,stop_dict)
    print(f"#{test_case} {result}")






