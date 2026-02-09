n, m = map(int,input().split())

# 최대가 되는 값 = 우하단 경계
# 곱의 합을 구하라
# 값이 음수일수 있으니 우하단이 정답이 아니다

mat_n = [ list(map(int,input().split())) for _ in range(n) ]
mat_m = [ list(map(int,input().split())) for _ in range(m) ]


max_val = 0
for nx in range(m-n+1):
    for ny in range(m-n+1):
        sum_val = 0
        for i in range(nx,nx+n):
            for j in range(ny,ny+n):
                n_val = mat_n[i-nx][j-ny]
                m_val = mat_m[i][j]
                print('좌표',i,j)
                print('값',n_val,m_val)
                sum_val += n_val * m_val
        print(sum_val)
        if sum_val > max_val:
            max_val = sum_val

print(max_val)