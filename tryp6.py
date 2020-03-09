num=int(input("How many terms? "))

a=0;
b=1;
count=0;

if(num<=0):
    print('Enter positive numbers');
elif(num==1):
    print(a);
else:
    for count in range(count,num):
         print(a)
         c=a+b;
         a=b;
         b=c;