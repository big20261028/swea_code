### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간
세로로도 찾아야 한다
총 글자판과 찾아야하는 회문 길이는 다르다.

'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    matrix = [ list(input()) for _ in range(n) ]
    #print(matrix)

    # 가로와 세로로 탐색해야 한다.
    # 세로열 먼저 추가
    target_list = [ list(matrix[row][col] for row in range(n) ) for col in range(n) ]
    #print(target_list)
    target_list.extend(matrix)

    # 모두 문자열로 변화
    target_list = [ ''.join(item) for item in target_list ]

    # print(target_list)
    # print(len(target_list))

    target_text = []
    for item in target_list:
        for a in range(n-m+1):
            target_text.append(item[a:a+m])

    # print(target_text)
    # print(len(target_text[0]))

    wrong_list = []
    for item in target_text:
        for a in range(m//2):
            b = m-1-a
            if item[a] != item[b]:
                wrong_list.append(item)
                break

    result = [item for item in target_text if item not in wrong_list ]
    print(f"#{test_case} {result[0]}")