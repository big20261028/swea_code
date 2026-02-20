import sys
sys.stdin = open('sample_input.txt','r')

def is_build_road(arr):
    used_ground = [False] * N
    for i in range(N - 1):
        if abs(arr[i] - arr[i + 1]) > 1:
            return False

        # 다음 좌표가 더 클 때
        if arr[i] < arr[i + 1]:
            for m1 in range(X):
                # 현재 좌표 포함 X개 조사 시도
                ni = i - m1
                # 범위 벗어나면 False 리턴
                if not (0 <= ni < N):
                    return False
                # 값이 i의 값과 다르면 False 리턴
                if arr[i] != arr[ni]:
                    return False
                # 좌표에 이미 경사로가 설치되어 있다면 False
                if used_ground[ni]:
                    return False
                # 모두 회피했다면 경사로 설치
                used_ground[ni] = True

        # 다음 좌표가 더 작을 때
        elif arr[i] > arr[i + 1]:
            for m2 in range(1,X+1):
                # 다음 좌표 포함 X개 조사 시도
                ni = i + m2
                # 범위 벗어나면 False 리턴
                if not (0 <= ni < N):
                    return False
                # 값이 i+1의 값과 다르면 False 리턴
                if arr[i+1] != arr[ni]:
                    return False
                # 좌표에 이미 경사로가 설치되어 있다면 False
                if used_ground[ni]:
                    return False
                # 모두 회피했다면 경사로 설치
                used_ground[ni] = True

    return True

T = int(input())
for tc in range(1,T+1):
    # 지형 크기, 경사로 길이
    N,X = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    line_list = list(zip(*matrix))
    line_list.extend(matrix)
    #print(len(line_list))
    cnt = 0
    for line in line_list:
        if is_build_road(line):
            cnt += 1

    print(f'#{tc} {cnt}')