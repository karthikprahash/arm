# arm
a=int(input())
temp=a
rev=0
while(a>0):
    rem=a%10
    rev=rev+rem**3
    a=a//10
if(temp==rev):
    print('yes')
else:
    print('no')
