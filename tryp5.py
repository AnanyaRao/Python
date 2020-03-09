num=input("Enter a number:");
num=int(num);
i=2;
flag=0;
for i in range(i,num,1):
    if(num%i==0):
        flag=1;
        break;
if(flag==0):
    print('Prime number');
else:
    print('Not a prime number');