def generate_fibanacci(n):
    list_a=[];
    i=1;
    a=0;
    b=1;
    c=0;
    if n==1:
        print(n)
        list_a.append(n);
    else:
        for i in range(i,n+1):
            list_a.append(a);
            c=a+b;
            a=b;
            b=c;
        
    return list_a;

n=int(input("How many terms:"))
list_a=generate_fibanacci(n)
print("The fibanacci numbers are:")
i=0;
for i in range(i,len(list_a)):
    print(list_a[i])