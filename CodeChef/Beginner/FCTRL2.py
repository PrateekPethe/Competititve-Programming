#Small Factorials. Link - https://www.codechef.com/problems/FCTRL2

n=int(input())
def facto(a):
    mul=1
    while(a>0):
        mul=mul*a
        a=a-1
    return(mul)
for i in range(n):
    k=int(input())
    print(facto(k))
