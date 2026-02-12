import sys
sys.stdin = open('sample_input.txt','r')

from itertools import combinations

T = int(input())
for tc in range(1,T+1):
    # N:벌통 개수, M:한번에 채취할 벌통 개수 , C:채집 가능한 양
    N,M,C = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    max_honey = 0

    # 첫 일꾼의 좌표 구하기
    for i_1 in range(N):
        for j_1 in range(N-M+1):
            #total_honey = 0

            # 첫 일꾼이 채취할 벌통 슬라이싱
            alpha = matrix[i_1][j_1:j_1+M]
            # 선택한 벌통들의 최대 수익 산출
            # itertools의 combinations 함수 사용
            # 조합들 구하기
            alpha_max = 0
            # 1개부터 M개의 조합
            for num in range(1,M+1):
                # combinations([1,2,3],1) 의 결과값 [[1],[2],[3]]
                targets = combinations(alpha,num)
                #print(list(targets))
                # 구해진 조합별 수익 구하기
                for item in targets:
                    if sum(item) > C:
                        continue
                    benefit = [ x**2 for x in item ]
                    total = sum(benefit)
                    alpha_max = max(alpha_max,total)

            # 두번째 일꾼의 좌표 구하기
            for i_2 in range(i_1,N):
                for j_2 in range(N-M+1):
                    # 만약 같은 행에 첫 일꾼이 있고, 첫 일꾼이 채집하는 통의 좌표보다 작으면 continue
                    if i_2 == i_1 and j_2 < j_1+M:
                        continue

                    beta = matrix[i_2][j_2:j_2+M]
                    beta_max = 0
                    for num in range(1,M+1):
                        targets = combinations(beta,num)
                        for item in targets:
                            if sum(item) > C:
                                continue
                            benefit = [ x**2 for x in item ]
                            total = sum(benefit)
                            beta_max = max(beta_max,total)

                    # 첫번째 통 고정/ 두번째 통을 돌며 찾기
                    # 첫 일꾼의 최대 이익과 두번째 일꾼의 최대 이익을 합하기
                    # 이 값이 기록된 최대 이익보다 크면 바꾸기
                    max_honey = max(max_honey, (alpha_max + beta_max))

    print(f'#{tc} {max_honey}')





