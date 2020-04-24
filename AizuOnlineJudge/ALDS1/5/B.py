N = int(input())
S = [int(s) for s in input().split()]

snt = 10 ** 9 + 1
cnt = 0

def merge(S, N, left, mid, right):
    global cnt
    L = S[left:mid] + [snt]
    R = S[mid:right] + [snt]
    i, j = 0, 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
            S[k] = L[i]
            i += 1
        else:
            S[k] = R[j]
            j += 1

def merge_sort(S, N, left, right):
    if left + 1 < right:
        mid = int((left + right) / 2)
        merge_sort(S, N, left, mid)
        merge_sort(S, N, mid, right)
        merge(S, N, left, mid, right)

merge_sort(S, N, 0, N)

print(*S)
print(cnt)