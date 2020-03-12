list_a=[7,9,11,13,15,20,23];
i=0;
k=2;
j=0;
flag=1;
list_b=[];
for i in range(i,len(list_a)):
    for k in range(2,list_a[i]):
        if(list_a[i]%k==0):
            flag=1;
            break;
        else:
            flag=2;
    if(flag==2):
        list_b.append(list_a[i]);
                
print(list_b)