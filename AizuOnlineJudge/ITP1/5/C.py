while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for h in range(H):
        for w in range(W):
            if h % 2 == 0:
                print('#.'[w % 2], end='')
            if h % 2 != 0:
                print('.#'[w % 2], end='')
        print()
    print()
