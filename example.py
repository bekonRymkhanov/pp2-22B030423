correct=0
num_of_q=0

exam={}
while True:
    question=input("question:")
    ans=input("answer of question:")
    exam[question]=ans
    next_opper=input("print 'next' to add another question,print 'start' to start a test: ")
    num_of_q+=1
    if(next_opper=="next"):
        continue
    elif(next_opper=="start"):
        break
    else:
        print("i think you mean 'next',so ok.")
for keys in exam:
    print(keys,": ")
    answer=input()
    if(exam[keys]==answer):
        correct+=1
percent=float(correct/num_of_q)*100
if percent>=70.0:
    print("congrats you have ",percent," %")
else:
    print("you lost")
