def words_count(sentence):
    sent=sentence.split();
    dict_a={};
    c=[];
    
    for i in range(0,len(sent)):
        c.append(len(sent[i]));
        element=c[i]
        f=c.count(element)
        dict_a.update({element:f})
    
    return dict_a;

sent="I love python and it so easy to learn";
#sent=input("Enter a sentence:");
dict_a=words_count(sent);
print("The word count is:" +str(dict_a))