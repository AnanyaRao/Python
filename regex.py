import re
if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"A\dl","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"A\d+","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"A\d?i","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"A\d{3}i","A223irline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"A[4-8]l","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"^A","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"e$","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"Air\s","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")
print("-------------------------------------")
if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")