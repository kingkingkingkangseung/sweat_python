import sys

sys.setrecursionlimit(10 ** 5)

dp =[0] * 10001

def fibo(n):
    if dp[n]:
        return dp[n]
    if n <= 1:
        return n
    dp[n]=fibo(n-1)+fibo(n-2)

    return dp[n]

print(fibo(int(input())))