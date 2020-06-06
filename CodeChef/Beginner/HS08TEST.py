#ATM. Link - https://www.codechef.com/problems/HS08TEST
x,y=map(float,input().split())
if(0<x and x<=2000):
    if(0<=y and y<=2000):
        if(x>=(y-0.5) or x%5!=0):
            print('%0.2f'%y)
        else:
            y=y-x-0.5
            print('%0.2f'%y)
