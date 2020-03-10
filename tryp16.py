no =101;
nop=int(input("Enter the no of passenger travelling:"));
i=1;
list_p=[];
for i in range(i,nop+1):
    airline=input("Enter airline:");
    src=input("Enter src:");
    dst=input("Enter destination:");
    str1=airline+src[0:3]+dst[0:3]+str(no);
    no=no+1
    list_p.append(str1);

if(no>=105):
    print(list_p[-5:len(list_p)])
else:
    for i in range(0,len(list_p)):
        print(list_p[i])