list_a=[1,1,5,100,-20,-20,6,0,0]
#list_a=list(input("Enter a list:"))
print(list_a)
i=0;
count=0;
for i in range(0,len(list_a)):
    if(i<len(list_a)-1):
        if list_a[i] == list_a[i+1]:
            count+=1;
print(count)