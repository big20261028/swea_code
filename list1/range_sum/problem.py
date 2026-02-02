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
    N, M = map(int,input().split())
    num_list = list(map(int, input().split()))

    max_sum = 0
    min_sum = sum(num_list)
    for i in range(N):
        sum_data = 0
        if i+M <= N:
            for idx in range(i,i+M):
                sum_data += num_list[idx]
        #print('sum data: ',sum_data)
        if sum_data > max_sum:
            max_sum = sum_data
            #print('max값 갱신',max_sum)
        if sum_data < min_sum and sum_data != 0:
            min_sum = sum_data
            #print('min값 갱신', min_sum)

    result = max_sum - min_sum
    print(f"#{test_case} {result}")
