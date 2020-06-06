t = int(input())
if t >= 1 and t <=100:
    for i in range(t):
        n,k = map(int,input().split())
        if n>=1 and n <=10000 and k>=1 and k<=1000:
            lst = list(map(int,input().split()))
            lstsum  = sum(lst)
            for i in range(len(lst)):
                if lst[i]>=1 and lst[i]<=1000:
                    if lst[i]>k:
                        lst[i]=k
            lst2sum = sum(lst)
            print(lstsum - lst2sum)
