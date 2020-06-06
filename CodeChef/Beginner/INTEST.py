#Enormous Input. Link - https://www.codechef.com/problems/INTEST
n,k=map(int,input().split())
a=[]
count=0
if(0<=k and k<=10000000):
    for i in range(n):
        inpt=int(input())
        a.append(inpt)
    for i in range(n):
        if(a[i]%k==0):
            count=count+1
        else:
            count=count 
print(count)    
