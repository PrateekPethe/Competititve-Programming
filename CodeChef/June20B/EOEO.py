#The Tom and Jerry Game. Link - https://www.codechef.com/JUNE20B/problems/EOEO/
t = int(input())
for i in range(t):
    ts = int(input())
    if ts%2 != 0 :
        js = (ts - 1) // 2
    else:
        while(ts%2 == 0):
            ts = ts//2
        js = (ts - 1)//2
    print(js)
