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
    a,b = input().split()
    cnt = len(a)
    i = 0
    while i <= len(a)-len(b):
        if a[i:i+len(b)] == b:
            i += len(b)
            cnt -= len(b)-1
            continue
        i += 1

    result = cnt
    print(f"#{test_case} {result}")
