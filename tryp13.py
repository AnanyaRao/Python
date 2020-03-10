def right_shift(num,n):
    flag=num>>n;
 
    return flag;

num=int(input('Enter the num:'))
n=int(input('Enter the n:'))
flag=right_shift(num,n);
print("The right shifted value is:",flag);