cash=int(input())
left=1000-cash
cnt = 0

# while left > 0:
#     if left > 500:
#         left-=500
#         n=0
#         n+=1
#         if(left>=100):
#             left%=100
#             n+=left
#             if(left)

while left > 0:
    if left >= 500:
        left-=500
        cnt+=1
    elif left >= 100:
        left-=100
        cnt+=1
    elif left >= 50:
        left-=50
        cnt+=1
    elif left >= 10:
        left-=10
        cnt+=1
    elif left >= 5:
        left-=5
        cnt+=1
    else:
        left-=1
        cnt+=1
print(cnt)
        
    
