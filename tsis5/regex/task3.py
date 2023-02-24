import re
with open(file='row.txt',mode='r',encoding='utf8') as f:
    fil=f.read()
patt='[a-z]+[_]'
text='srtgrtg srghsrhrth rghrhr rtghrgd_ rthtKKV_'
print(re.findall(patt,text)[0])
print(re.findall(patt,fil))



