def find_common_characters(msg1,msg2):
    msg3="";
    for i in range(0,len(msg1)):
        for j in range(0,len(msg1[i])):
            if(msg2.find(msg1[i][j])>0 and msg1[i][j]!=" "):
                if msg1[i][j] in msg3:
                    pass;
                else:
                    msg3+=msg1[i][j];
    if(msg3!=""):
        return msg3;
    else:
        return -1;

msg1="I like Python";
msg2="Java is a very popular language";
msg=find_common_characters(msg1,msg2);               
print(msg)