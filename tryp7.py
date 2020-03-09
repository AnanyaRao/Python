sal=int(input("Enter Salary "));
jb=int(input("Enter Job level "));
if(jb==3):
    hk=0.15*sal+sal;
elif(jb==4):
    hk=0.07*sal+sal;
elif(jb==5):
    hk=0.05*sal+sal;
else:
    hk=0+sal;
print('Updated salary of jb '+str(jb)+' is '+str(hk))