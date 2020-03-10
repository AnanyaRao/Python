def translate(b_dict,list_words):

  splittedStr = list_words.split(" ")
  print(splittedStr)
  translatedStr = []

  for i in splittedStr:

    if i in b_dict:
      translatedStr.append(b_dict[i])

  return " ".join(translatedStr)


EngDict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
Inp= "merry christmas & Happy New Year"

a=translate(EngDict,Inp.lower())
print("Translated sweedish words: "+ a);