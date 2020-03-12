def find_pairs_of_numbers(num_list,n):
    list_n=[];
    sum1=0;
    count=0;
    for i in range(0,len(num_list)):
        for j in range(i+1,len(num_list)):
            sum1=num_list[j]+num_list[i];
            #print(sum1);
            if(sum1==n):
                count+=1;
    
    if(sum1!=0):
        return count;
    else:
        return 0;
        
num_list=[3, 4, 1, 8, 5, 9, 0, 6];
n=9;
msg=find_pairs_of_numbers(num_list,n);               
print(msg)