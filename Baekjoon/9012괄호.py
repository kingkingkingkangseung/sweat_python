n = int(input())

for i in range(n):
    stk = []
    a = input()

    for j in a:
        if j=='(':
            stk.append('(')

        elif j==')':
            if stk:
                stk.pop()
            else:
                print("NO")
                break

    else:  
        if a and not stk:
            print("YES")
        else:
            print("NO")
