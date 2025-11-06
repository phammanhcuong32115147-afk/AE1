dd,mm,yy=map(int,input().split())
n=1
tong=0
def thang(a,b):
    if a==2:
        if str(b)[-1:-3:-1]=='00' and b%400==0:
            return 29
        elif b%4==0:
            return 29
        else:
            return 28
    elif a in [4,6,9,11]:
        return 30
    else:
        return 31
while n<mm:
    tong+=thang(n,yy)
    n+=1
else:    
    tong+=dd
ct=yy+((yy-1)/4)-((yy-1)/100)+((yy-1)/400)+tong
if int(ct)%7==1:
    print('Chủ Nhật')
elif int(ct)%7==0:
    print('Thứ 7')
else:
    print('Thứ',int(ct)%7)
        
    
