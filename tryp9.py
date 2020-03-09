def find_sum(num):
    total=0;
    while(num):
        rem=num%10;
        total=rem+total;
        num//=10;
    return total;

num=int(input("Enter a number:"))
sum1=find_sum(num)
print('The sum of number is',sum1)