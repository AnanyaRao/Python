def encrypt_sentence(msg):
    list_a=msg.split()
    list_b=[];
    list_odd=[];
    list_even=[];
    q=""
    i=0;
    j=0;
    msg=""
    for i in range(0,len(list_a),2):
         list_a[i]=list_a[i][::-1]
         list_odd.append(list_a[i])
    for i in range(1,len(list_a),2):
        for j in range(0,len(list_a[i])):
            if(list_a[i][j]=='a' or list_a[i][j]=='e' or list_a[i][j]=='i' or list_a[i][j]=='o' or list_a[i][j]=='u'):
                q+=list_a[i][j];
            else:
                msg+=list_a[i][j];
        msg=msg+q;
        list_even.append(msg)
        q="";
        msg="";
        
    for i in range(0,(len(list_even))):
        list_b.append(list_odd[i])
        list_b.append(list_even[i])
        

    return " ".join(list_b);
    

#msg="the sun rises in the east"
msg=input("Enter a statement:")
ans=encrypt_sentence(msg);

print("The returned string:"+ans);

