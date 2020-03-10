def proper_devisor(num):
    list_a=[];
    i=1;
    for i in range(i,num):
        if(num%i==0):
            list_a.append(i);
    return list_a;

num=int(input("Enter the number:"))
list_a=proper_devisor(num)
print("The proper divisors are:")
i=0;
for i in range(i,len(list_a)):
    print(list_a[i])