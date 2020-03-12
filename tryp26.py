import re;

def vowel_count(sentence):
    sent=sentence.split();
    dict_a={};
    c=[];
    vowel=0;
    odd=0;
    other=len(sent)-1;
  
    for i in range(0,len(sent)):
        for j in range(0,len(sent[i])):
            
            if(re.search(r"[aeiouAEIOU]",sent[i][j])!=None):
                vowel+=1;
            elif(re.search(r"[/+/-/;/*/@/#/!/$]",sent[i][j])!=None):
                other+=1;
            elif(re.search(r"[^aeiouAEIOU]",sent[i][j])!=None):
                odd+=1;
            
                
        dict_a.update({"others":other,"consonents":odd,"vowel":vowel})
    
    return dict_a;

sent="I love python and it so easy to ++$learn";
#sent=input("Enter a sentence:");
dict_a= vowel_count(sent);
print("The word count is:" +str(dict_a))
