import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n,x = map(int,input().split())

    matrix = [ list(map(int,input().split())) for _ in range(n) ]

    from pprint import pprint
    # pprint(matrix)
    # print('-')

    lines = list(zip(*matrix))
    # pprint(lines)
    lines.extend(matrix)

    total = 0

    # 가로세로 한줄씩 가져와서 검사
    for line in lines:
        flag = True
        temp_list = []
        for i in range(n-1):
            # 현재 인덱스와 다음 인덱스가 같으면 continue
            if line[i] == line[i+1]:
                continue
            # 현재 인덱스와 다음 인덱스의 차이가 2 이상이면 break
            if line[i] < line[i+1]-1 or line[i] > line[i+1] + 1:
                flag = False
                break

            # 현재 인덱스가 다음 인덱스보다 큰 경우
            if line[i] > line[i+1]:
                height = line[i+1]
                # 다음 인덱스 x개 검사
                cnt = 0
                for idx in range(i+1,i+x+1):
                    if 0 <= idx < n and height == line[idx] and idx not in temp_list:
                        cnt += 1
                        temp_list.append(idx)
                if cnt != x:
                    flag = False
                    break

            # 현재 인덱스가 다음 인덱스보다 작은 경우
            elif line[i] < line[i+1]:
                height = line[i]
                cnt = 0
                for idx in range(i-x+1,i+1):
                    if 0 <= idx < n and height == line[idx] and idx  not in temp_list:
                        cnt += 1
                        temp_list.append(idx)
                if cnt != x:
                    flag = False
                    break
        if flag:
            total += 1

    print(f'#{tc} {total}')