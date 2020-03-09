def check_amicable_numbers(num1, num2):
    flag=False;
    i=1;
    j=1;
    sum1=0;
    sum2=0;
    for i in range(i,num1):
        if(num1%i==0):
            sum1+=i;
    for j in range(j,num2):
        if(num2%j==0):
            sum2+=j;
    
    #print(sum1,sum2,num1,num2);
    if(num1==sum2 and num2==sum1):
        flag=True;
    return flag;

num1=int(input('Enter the number1:'))
num2=int(input('Enter the number2:'))
flag=check_amicable_numbers(num1, num2);
if(flag):
    print('Amicable Numbers');
else:
    print('Not Amicable Numbers')
