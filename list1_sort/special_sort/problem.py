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

    arr.sort()
    reverse_arr = arr[::-1]

    # print(arr)
    # print(reverse_arr)

    result = []
    for i in range(5):
        result.append(reverse_arr[i])
        result.append(arr[i])
    #print(result)
    result = " ".join(map(str,result))

    print(f"#{test_case} {result}")
