def check_strong_number(num):
    flag=False;
    sum1=0;
    num1=num;
    while(num):
        rem=num%10;
        i=1;
        fact=1;
        for i in range(i,rem+1):
            fact=fact*i;
        sum1=sum1+fact;
        num//=10;
  #  print(sum1,num1);
    if(num1==sum1):
        flag=True;
    return flag;

num=int(input('Enter the num:'))

flag=check_strong_number(num);
if(flag):
    print('Strong Numbers');
else:
    print('Not Strong Numbers')