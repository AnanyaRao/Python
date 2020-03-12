str1="The count is999 what we find here";
i=0;
count=0;
for i in range(len(str1)):
    if(str1[i].isalpha()):
        count+=1;
print("The number is:"+str(count));