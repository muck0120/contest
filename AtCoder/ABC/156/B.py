# B - Digits

N, K = map(int, input().split())
ans = 0
while True:
    N = N // K
    ans += 1
    if N == 0:
        break
print(ans)