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
    n = int(input())
    # 작업시간 s, 종료시간 e
    tasks = [ tuple(map(int, input().split())) for _ in range(n) ]
    # 끝나는 시간 기준으로 정렬
    tasks.sort(key=lambda x : x[1])

    #print(tasks)

    end_t = 0
    cnt = 0

    for s,e in tasks:
        if s >= end_t:
            end_t = e
            cnt += 1

    result = cnt
    print(f"#{test_case} {result}")


    # tasks_dict = { s:e for s,e in tasks }
    # print(tasks_dict)
    # max_cnt = 0
    # for s,e in tasks_dict.items():
    #     print(s,e)
    #     cnt = 1
    #     while True:
    #         #print('while문 시작지점')
    #         for t in range(e,25):
    #             print(t)
    #             if tasks_dict.get(t,'X') != 'X':
    #                 e = tasks_dict.get(t)
    #                 cnt += 1
    #                 break
    #         # 한바퀴 돌고도 e에서 24까지 일치하는 s값이 없을경우 종료
    #         else:
    #             break
    #     if max_cnt < cnt :
    #         max_cnt = cnt

    # result = max_cnt
    # print(f"#{test_case} {result}")
