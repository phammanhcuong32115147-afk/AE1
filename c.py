b=input()
c=input()
def mahoa(a):
    chuoi=''
    tong=1
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            tong+=1
        else:
            chuoi+=str(tong)+a[i-1]
            tong=1
    chuoi+=str(tong)+a[-1]
    return chuoi
print(mahoa(b))
for k in range(len(c)):
    if c[k].isdigit():
        print(c[k+1]*int(c[k]),end='')

