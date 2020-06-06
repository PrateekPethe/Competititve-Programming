#Turbo Sort. Link - https://www.codechef.com/problems/TSORT

n=int(input())
l = []
for i in range(n):
    k=int(input())
    l.append(k)
l.sort()
for j in l:
    print(j)
