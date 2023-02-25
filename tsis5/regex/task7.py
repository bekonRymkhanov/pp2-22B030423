import re
import string
with open(file='row.txt',mode='r',encoding='utf8') as f:
    rowtxt=f.read()
text='hello_my_name_is'
patt='_'
words=list(re.split(patt,text))
for  i in range(len(words)):
    words[i]=words[i].capitalize()
word=''.join(words)
print(word)
    
    

