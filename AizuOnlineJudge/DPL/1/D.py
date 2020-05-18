import bisect

INF = 10 ** 9 + 1

N = int(input())
S = [int(input()) for l in range(N)]
L = [S[0]]

for i in range(1, N):
    if L[-1] < S[i]:
        L.append(S[i])
    else:
        L[bisect.bisect_left(L, S[i])] = S[i]

print(len(L))
