def factorial(num):
    fact=1;
    i=1;
    for i in range(i,num+1):
        fact=fact*i;
    return fact;
    
num=int(input('Enter the number:'))
fact=factorial(num);
print('The factorial of the number is:',fact)