import sys

sys.stdin = open('sample_input.txt', 'r')
'''
시간을 1초씩 진행시킨다.
고객 리스트를 deque로 변환 후 sort(), 매 시간마다 인덱스 0번과 비교하여
값이 같은 경우 popleft(). 인덱스로 비교하기 전에 deque의 길이가 0보다 큰지 확인

고객 정보를 담고 있는 딕셔너리를 만들기
해당 딕셔너리를 접수창구 or 정비창구 인덱스와 같은 곳에 넣고 빼기
매번 루프마다 a1_zone[0][end]로 value 뽑아와서 검사. 같으면 빼서 다음 공정으로


'''
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    # N:접수창구 수 M:정비창구 수 K:고객 수
    # A:타겟접수창구 B: 타겟정비창구
    N, M, K, A, B = map(int, input().split())
    # 접수창구 N개의 고장 접수 시간
    a1 = list(map(int, input().split()))
    # 정비창구 M개의 정비 소요 시간
    b1 = list(map(int, input().split()))
    # 각 고객 k명의 차량 정비소 방문 시간
    t1 = list(map(int, input().split()))

    # 고객별 딕셔너리 정보로 변경
    customers = deque()
    for i, t in enumerate(t1):
        customers.append({
            'num': i + 1,
            'arrive': t,
            'visit_a': -1,
            'visit_b': -1,
            'end': -1
        })

    # 접수창구와 정비창구 빈리스트 생성
    a2 = [0] * N
    b2 = [0] * M

    # 접수창구 대기실, 정비창구 대기실 생성
    w_a = deque()
    w_b = deque()

    complete = 0
    t = 0
    total = 0

    while complete < K:
        # 0초부터 시작

        # 접수창구 처리
        for i in range(N):
            # 창구에 고객 있고, 끝날 시간이면
            if a2[i] != 0 and a2[i]['end'] == t:
                customer = a2[i]
                a2[i] = 0
                # 완료한 고객은 일단 정비 대기실 뒤로 가서 줄서기
                w_b.append(customer)

        # 정비창구 처리
        for i in range(M):
            # 창구에 고객 있고, 끝날 시간
            if b2[i] != 0 and b2[i]['end'] == t:
                customer = b2[i]
                b2[i] = 0

                # 완료한 고객 숫자 증가
                complete += 1
                # 고객이 타겟과 같은 경로를 거쳐왔는지 조사
                if customer['visit_a'] == A and customer['visit_b'] == B:
                    total += customer['num']

        # 정비창구 채우기
        for i in range(M):
            # 해당 인덱스가 비었고, 정비대기실에 사람이 있다면
            if b2[i] == 0 and w_b:
                customer = w_b.popleft()
                customer['visit_b'] = i + 1
                customer['end'] = t + b1[i]
                b2[i] = customer

        # 올 손님이 있고, 그 손님이 도착할 시간이라면
        while customers and customers[0]['arrive'] == t:
            # 일단 손님 대기실로 이동
            w_a.append(customers.popleft())

        # 접수창구 채우기
        for i in range(N):
            # 창구가 비었고 접수 대기실에 사람이 있다면
            if a2[i] == 0 and w_a:
                customer = w_a.popleft()
                customer['visit_b'] = i + 1
                customer['end'] = t + a1[i]
                a2[i] = customer

        # # 접수가 끝났는지 확인
        # for i in range(N):
        #     # 비어있지 않은 것만 검사 / t와 끝나는 시간이 같으면
        #     if a2[i] != 0 and a2[i]['end'] == t:
        #         # 정비소에 빈 자리가 있으면 들어가고, 아니면 정비창구 대기실로
        #         if 0 in b2:
        #             idx = b2.index(0)
        #             customer = a
        #             customer['visit_b'] = idx
        #             customer['end'] = b1[idx] + t
        #             b2[idx] = customer
        #         else:
        #             # 정비창구 대기실로 이동
        #             w_b.append(a)
        #
        #         # 접수창구 대기실에 사람이 있을경우
        #         if w_a:
        #             # 현재 시간을 기준으로 시작 끝 설정
        #             customer = w_a.popleft()
        #             customer['visit_a'] = i
        #             customer['end'] = t + a1[i]
        #             a = customer
        #         # 없으면 값을 0으로 초기화
        #         else:
        #             a = 0
        #
        # # 정비가 끝났는지 확인
        # for i,b in enumerate(b2):
        #     # 비어있지 않은 것만 검사 / t와 끝나는 시간이 같으면
        #     if b != 0 and b['end'] == t:
        #         # 정비 끝난 고객 수 + 1
        #         complete += 1
        #         # 정비를 마친 고객이 분실 고객과 같은 경로를 거쳤는지 확인
        #         if b['visit_a'] == A and b['visit_b'] == B:
        #             # 고객번호를 total에 누적
        #             total += b['num']
        #
        #
        #         # 정비창구 대기실에 사람이 있을경우
        #         if w_b:
        #             # 현재 시간을 기준으로 시작 끝 설정
        #             customer = w_b.popleft()
        #             customer['end'] = t + b1[i]
        #             b = customer
        #         else:
        #             b = 0
        #
        #
        #
        # while len(t1) and t == t1[0]:
        #     customer = {
        #         'num' : cus_num,
        #         'visit_a' : -1,
        #         'visit_b' : -1,
        #         'end' : None
        #     }
        #     cus_num += 1
        #     #손님이 도착하자마자 들어갈 자리가 있을경우
        #     if 0 in a2:
        #         idx = a2.index(0)
        #         customer['visit_a'] = idx
        #         customer['end'] = a1[idx] + t1.popleft()
        #         a2[idx] = customer
        #     # 자리가 없을 경우 대기실로
        #     else:
        #         w_a.append(customer)

        # 시간 경과
        t += 1

    print(f'#{tc} {total}')

