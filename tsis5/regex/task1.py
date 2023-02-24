import re
with open (file='row.txt',mode='r',encoding='utf8') as f:
    fil = f.read()
patt='a[b]*'
print(re.search(patt,fil)[0])
