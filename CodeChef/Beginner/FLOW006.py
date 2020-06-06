#Sum of Digits. Link - https://www.codechef.com/problems/FLOW006

n=int(input())
def sumre(a):
    sumt=0
    while(a>0):
        d=a%10
        sumt=sumt+d
        a=a//10
    return(sumt)
for i in range(n):
    k=int(input())
    print(sumre(k))
