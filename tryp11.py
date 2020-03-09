def is_palindrome(num):
    flag=False;
    i=1;
    num1=num;
    sum1=0;
    while(num):
        rem=num%10;
        sum1=sum1*10+rem;
        num//=10;
    # print(sum1,num1)
    if(num1==sum1):
        flag=True;
    return flag;

num=int(input('Enter the number:'))
flag=is_palindrome(num);
if(flag):
    print('Palindrome');
else:
    print('Not palindrome')
