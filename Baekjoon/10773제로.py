k=int(input())

for i in range(k):
    stk = []
    a = input()

    if j== 0:
        if stk:
            stk.pop()
    else:
        stk.append(a)
print(sum(stk))