def max(a, b):
    while b!=0:
        x = a%b
        max(b, x)
    return b

def min(a, b):
    minval=(a*b)/max(a,b)
    return minval

a, b = map(int, input().split())
print(max(a,b))
print(min(a,b))

        
