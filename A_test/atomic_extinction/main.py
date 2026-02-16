import sys
sys.stdin = open('sample_input.txt','r')

'''
원자들이 소멸되면서 방출하는 에너지의 총합 출력
얼마나 걸리는지는 중요하지 않음,
두 좌표가 만날 수 있는지 없는지, 만나더라도 어떤 원자와 먼저 반응해서 사라지는지
시간을 2000초 동안 진행시키며 실험.

'''

T = int(input())

for tc in range(1,T+1):
    # 원자 수
    N = int(input())
    # x 위치, y 위치, 이동 방향, 보유 에너지 K
    atomics = [ list(map(int,input().split())) for _ in range(N) ]
    # 이동 방향 필터링
    # 상(0), 하(1), 좌(2), 우(3)
    dxy = {
        0 : (0,0.5),
        1 : (0,-0.5),
        2 : (-0.5,0),
        3 : (0.5,0),
    }
    # 딕셔너리로 변환
    atoms = {}
    # (x,y) = {dr : 0 , power : K}
    for x,y,dr,k in atomics:
        atoms[(x,y)] = {
            'dr' : dxy[dr],
            'power' : k
        }

    t = 0

    powers = 0
    while t <= 4000:
        t += 1
        temp_dict = {}
        explode_atoms = {}
        for (x,y),item in atoms.items():
            dx,dy = item['dr']
            nx = x + dx
            ny = y + dy
            # 이동할 좌표에 이미 원소가 있다면
            if (nx,ny) in temp_dict:
                # dr,power값 가지고 있는 dict 데이터 pop
                target = temp_dict.pop((nx,ny))
                # 폭팔 예정 원소의 폭팔 값을 저장
                explode_atoms[(nx,ny)] = item['power'] + target["power"]
            # 이동할 좌표가 폭팔할 좌표라면
            elif (nx,ny) in explode_atoms:
                explode_atoms[(nx,ny)] += item['power']
            # 아무것도 해당되는 것이 없다면
            else:
                temp_dict[(nx,ny)] = item

        # 이동할 좌표 리스트를 원소 리스트에 갱신
        atoms = temp_dict

        # 폭팔 처리
        for p in explode_atoms.values():
            #print(p)
            powers += p

    print(f'#{tc} {powers}')










