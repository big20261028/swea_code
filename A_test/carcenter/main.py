import sys
sys.stdin = open('sample_input.txt','r')
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
for tc in range(1, T+1):
    # N:접수창구 수 M:정비창구 수 K:고객 수
    # A:타겟접수창구 B: 타겟정비창구
    N,M,K,A,B = map(int,input().split())
    # 접수창구 N개의 고장 접수 시간
    a1 = list(map(int,input().split()))
    # 정비창구 M개의 정비 소요 시간
    b1 = list(map(int,input().split()))
    # 각 고객 k명의 차량 정비소 방문 시간
    t1 = list(map(int,input().split()))
    t1.sort()
    t1 = deque(t1)

    # 접수창구와 정비창구 빈리스트 생성
    a2 = [0] * N
    b2 = [0] * M

    # 접수창구 대기실, 정비창구 대기실 생성
    w_a = deque()
    w_b = deque()

    complete = 0
    t = 0
    while complete < len(t1):
        # 0초부터 시작

        # 접수가 끝났는지 확인
        for i,a in enumerate(a2):
            # 비어있지 않은 것만 검사 / t와 끝나는 시간이 같으면
            if a != 0 and a['end'] == t:
                # 정비창구 대기실로 이동
                w_b.append(a)
                # 접수창구 대기실에 사람이 있을경우
                if w_a:
                    # 현재 시간을 기준으로 시작 끝 설정
                    customer = w_a.popleft()
                    customer['start'] = t
                    customer['end'] = t + a1[i]
                    a = customer
                # 없으면 값을 0으로 초기화
                else:
                    a = 0

        # 정비가 끝났는지 확인
        for i,b in enumerate(b2):
            # 비어있지 않은 것만 검사 / t와 끝나는 시간이 같으면
            if b != 0 and b['end'] == t:
                # 정비 끝난 고객 수 + 1
                complete += 1
                # 정비창구 대기실에 사람이 있을경우
                if w_b:
                    # 현재 시간을 기준으로 시작 끝 설정
                    customer = w_b.popleft()
                    customer['start'] = t
                    customer['end'] = t + b1[i]
                    b = customer
                else:
                    b = 0



        while len(t1) and t == t1[0]:
            customer = {
                'visit_a' : None,
                'visit_b' : None,
                'start' : t1.popleft(),
                'end' : None
            }
            #손님이 도착하자마자 들어갈 자리가 있을경우
            if 0 in a2:
                idx = a2.index(0)
                customer['end'] = a1[idx] + customer['start']
                a2[idx] = customer
            # 자리가 없을 경우 대기실로
            else:
                w_a.append(customer)

        # 시간 경과
        t += 1



