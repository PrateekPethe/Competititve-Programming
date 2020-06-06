#Chef and Icecream link - https://www.codechef.com/JUNE20B/problems/CHFICRM/
t =  int(input())
for i in range(t):
    n = int(input())
    rs5coin = 0
    rs10coin = 0
    rs15coin= 0
    sale = list(map(int,input().split()))
    allsale = 1
    for j in range(len(sale)):
        if sale[j]==5:
            rs5coin = rs5coin+1
        elif sale[j]==10:
            if rs5coin>0:
                rs5coin = rs5coin - 1
                rs10coin = rs10coin + 1
            else:
                allsale =0
                break
        else:
            if sale[j]==15:
                if rs10coin>0:
                    rs10coin = rs10coin - 1
                    rs15coin = rs15coin + 1
                elif rs5coin>=2:
                    rs5coin = rs5coin - 2
                    rs15coin = rs15coin + 1
                else:
                    allsale = 0
                    break
    if allsale == 1:
        print('YES')
    else:
        print('NO')
