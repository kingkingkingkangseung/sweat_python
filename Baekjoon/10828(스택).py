# N=int(input())
# stk = []

# for i in range(N):
#     commands = input().strip()
#     parts = commands.split()

#     if parts[0] == "push":
#         value = int(parts[1])
#         stk.append(value)

#     elif parts[0] == "pop":
#         if stk:
#             print(stk.pop())
#         else:
#             print(-1)
    
#     elif parts[0] == "size":
#         print(len(stk))

#     elif parts[0] == "empty":
#         print(0 if stk else 1)

#     elif parts[0] == "top":
#         if stk:
#             print(stk[-1])
#         else:
#             print(-1)

import sys
input = sys.stdin.readline

N = int(input())
stk = []

for _ in range(N):
    parts = input().split()

    if parts[0] == "push":
        stk.append(int(parts[1]))

    elif parts[0] == "pop":
        print(stk.pop() if stk else -1)

    elif parts[0] == "size":
        print(len(stk))

    elif parts[0] == "empty":
        print(0 if stk else 1)

    elif parts[0] == "top":
        print(stk[-1] if stk else -1)
