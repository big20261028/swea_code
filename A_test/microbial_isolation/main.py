import sys
sys.stdin = open('sample_input.txt','r')
'''
M시간 후 남아 있는 미생물 수의 총 합
'''
T = int(input())
for tc in range(1,T+1):
    # 셀의 개수, 격리시간, 미생물 개수
    N,M,K = map(int,input().split())

    cell_dict = {}

    # 방향데이터 관리 편하게 필터링
    # 상하좌우 -> 상좌하우 인덱스로 변경
    dr_filter = { 1 : 0, 2 : 2, 3 : 1, 4 : 3}
    # 상좌하우
    dxy = [ (-1,0),(0,-1),(1,0),(0,1) ]

    for i in range(K):
        x,y,c,d = map(int,input().split())
        cell_dict[(x,y)] = {
            'count' : c,
            'max_reward' : c,
            'dr' : dr_filter[d]
        }

    t = 0

    while t < M:
        t += 1
        temp_dict = {}
        for (x,y),cell in cell_dict.items():
            nx = x + dxy[cell['dr']][0]
            ny = y + dxy[cell['dr']][1]
            # 약품셀에 동시에 2개의 군집이 도달하는 경우는 없다고 본다.
            # 고로 이미 이동한 군집과 이동할 군집의 데이터가 겹치는 경우를 먼저 본다.
            if (nx,ny) in temp_dict:
                # 이미 이동했던 미생물 군집의 최대값과 이동할 군집의 개수 비교
                # 최대값 비교 이유는 이미 한번 합쳤던 군집이어도 바뀌게끔
                if temp_dict[(nx,ny)]['max_reward'] < cell['count']:
                    temp_dict[(nx,ny)]['dr'] = cell['dr']
                    temp_dict[(nx,ny)]['max_reward'] = cell['count']
                temp_dict[(nx, ny)]['count'] += cell['count']
            else:
                # 만약 이동할 좌표가 약품셀이라면
                if nx==0 or nx==N-1 or ny==0 or ny==N-1:
                    # 미생물 수 반절로 나누기
                    count = cell['count']//2
                    # 나눈 값이 0이면 등록 안함
                    if count > 0 :
                        # 방향이 반대로 전환됨
                        temp_dict[(nx, ny)] = {
                            'count': count,
                            'max_reward': count,
                            'dr': (cell['dr']+2) % 4
                        }
                # 약품셀이 아니면
                else:
                    # 이동한 셀 데이터 추가
                    temp_dict[(nx,ny)] = {
                        'count' : cell['count'],
                        'max_reward' : cell['count'],
                        'dr' : cell['dr']
                    }
        cell_dict = temp_dict

    result = 0
    #print(cell_dict)
    # 남은 미생물 수 총합 출력
    for cell in cell_dict.values():
        #print(cell)
        result += cell['count']

    print(f'#{tc} {result}')

