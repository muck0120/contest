# D - Multiple of 2019

s = input()[::-1]
 
counts = [0] * 2019
counts[0] = 1

num, d = 0, 1

for char in s:
    num += int(char) * d
    num %= 2019
    d *= 10
    d%= 2019
    counts[num] += 1
 
ans = 0
for cnt in counts:
    ans += cnt * (cnt - 1) // 2
 
print(ans)