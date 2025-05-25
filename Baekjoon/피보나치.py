#n=int(input())
#s=0
#s[0]=0
#x=1
#while(s<=n):
#    s[x]=s[x-1]+s[x-2]
#    x+=1
#    print(s[x])



#재귀함수 (top-down)
    #1. 점화식 찾기
    #2. base-case 찾기 (첫번째는 0, 1)
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)  #점화식

print(fibo(int(input())))


