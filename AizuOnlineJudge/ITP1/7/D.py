n, m, l = map(int, input().split())
A = [[int(a) for a in input().split()] for _ in range(n)]
B = [[int(b) for b in input().split()] for _ in range(m)]
C = [[0] * l for _ in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for c in C:
    print(*c)