import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    atoms = {}
    # 상(0), 하(1), 좌(2), 우(3)
    # 0.5초로 변환
    dxy = [ (0,0.5),(0,-0.5),(-0.5,0),(0.5,0) ]

    for _ in range(N):
        x, y, dr, k = map(int,input().split())

        atoms[(x,y)] = {
            'dr' : dr,
            'k' : k,
        }

    t = 0
    total = 0

    while t <= 4000:
        t += 1

        dead_atoms = {}
        temp_dict = {}

        for (x,y), atom in atoms.items():
            dx,dy = dxy[atom['dr']]

            nx,ny = x + dx, y + dy

            if (nx,ny) in dead_atoms:
                dead_atoms[(nx,ny)] += atom['k']
            elif (nx,ny) in temp_dict:
                dead_atoms[(nx,ny)] = atom['k'] + temp_dict[(nx,ny)]['k']
                del temp_dict[(nx,ny)]
            else:
                temp_dict[(nx,ny)] = {
                    'dr' : atom['dr'],
                    'k' : atom['k'],
                }

        for dead_k in dead_atoms.values():
            total += dead_k

        atoms = temp_dict

    print(f'#{tc} {total}')






