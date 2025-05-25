# stk = []

# stk.append(1)
# stk.append(2)
# stk.append(3)
# stk.append(4)

# stk.pop()

# print(stk)


# #ctrl +k+c

##########################
# que = []

# que.append(1)
# que.append(2)

# que.pop(0)
# que.pop(0)  #index 0번째를 pop해라



# print(que)


from collections import deque

que=deque()

que.append(1)
que.append(2)
que.append(3)

que.popleft()
que.popleft()

print(que)