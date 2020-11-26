A = [1, 2, 2]
A.sort()
ans, chk, val = 1, 0, A[0]
for i in range(1, len(A)):
    if val == A[i]:
        if chk:
            continue
        chk = 1

    else:
        val = A[i]
        chk = 0
    ans += 1
if chk:
    ans -= 1
print(ans)