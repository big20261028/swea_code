### 제출 전에 지우기 ###
import sys
sys.stdin = open("input1.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    text = input()

    max_cnt = 0
    cnt = 0
    for char in text:
        #print(char)
        if char == '1':
            cnt += 1
            #print("연속된 1 갯수 증가::",cnt)
        else:
            cnt = 0

        if cnt > max_cnt:
            max_cnt = cnt
            #("최댓값 변화:", max_cnt)
    #print("loop end")


    # 조건 확인 실수
    # max_cnt = 0
    # start_char = text[0]
    # cnt = 0
    # for char in text:
    #     if char == start_char :
    #        cnt += 1
    #     else:
    #         start_char = char
    #         if max_cnt < cnt:
    #             max_cnt = cnt
    #         cnt = 1
    #     pass

    result = max_cnt
    print(f"#{test_case} {result}")
