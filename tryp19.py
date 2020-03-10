def leap_year(n):
    list_a=[];
    i=1;
    for i in range(n,n+16):
        if(i%4==0 and i%100!=0):
            list_a.append(i);
        elif(i%400==0):
            list_a.append(i);
   
    return list_a;

n=int(input("Enter the starting year:"))
list_a=leap_year(n)
print("The leeap years are:")
i=0;
for i in range(i,len(list_a)):
    print(list_a[i])