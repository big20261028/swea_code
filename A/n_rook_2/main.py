N = int(input()) # 세로크기
M = int(input()) # 가로크기
K = int(input()) # 룩의 수

from collections import defaultdict

'''
x딕셔너리와 y딕셔너리 만들기
키값 = 좌표값
벨류값 = 룩의 인덱스

x,y로 이루어진 set도 만들기

선택지
- 이번 줄에 혼자 놓여있기
- 이번 줄에 같이 놓여있기
- 이번 줄에 아무도 놓여있지 않기

일단 K//2 값보다 M, N 둘다 작으면 경우의 수 구할 수 없음?

첫 좌표값
for i in range(M)
for j in range(N):
모두 가능

두번째 좌표값
for i in range(M)
for j in range(N)
첫 좌표값 빼고 모두 가능

세번째 좌표값부터
만약 두번째 좌표값의 x or y가 첫 좌표값과 같다면
두 좌표값의 x,y 값은 못씀

계속 이중for문을 쓰면, 2번째에서 선택하고 넘어갔던 경우의 수를 다시 계산해올 수 있음


'''

def dfs(deps,i,j,subset):
    global total

    if deps == K:
        total += 1
        return

    for ni in range(M):
        if x_dict[ni] >= 2: continue
        for nj in range(N):
            if y_dict[nj] >= 2 : continue
            if visited[ni][nj]: continue

            visited[ni][nj] = True
            x_dict[ni] += 1
            y_dict[nj] += 1
            dfs(ni,nj, subset + ((ni, nj)))
            visited[ni][nj] = False
            x_dict[ni] -= 1
            y_dict[nj] -= 1


x_dict = defaultdict(int)
y_dict = defaultdict(int)
#pos_dict = {}

visited = [[False] * N for _ in range(M)]
total = 0

for i in range(M):
    for j in range(N):
        visited[i][j] = True
        x_dict[i] += 1
        y_dict[j] += 1
        dfs(1, i,j, ( (i,j) ))
        x_dict[i] -= 1
        y_dict[j] -= 1
