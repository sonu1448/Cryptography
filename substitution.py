f=open("key.txt","r")
f1=open("input.txt","r")
f2=open("output.txt","w")
key=f.read()
result=""
for i in f1:
    for j in i:
        if(j.isupper()):
            temp=(ord(j)-65)
            result+=key[temp]
        elif(j.islower()):
            temp=(ord(j)-97)
            result+=key[temp]
        else:
            result+=j
f2.write(result)

result2=""
for i in result:
    
    if(i.isupper()):
        temp=chr(ord('A')+key.find(i))
        result2+=temp
    elif(i.islower()):
        temp=chr(ord('A')+key.find(i))
        result2+=temp
    else:
        #print(i,key.find(i))
        result2+=i
#print(result2)
f3=open("decript.txt","w")
f3.write(result2)
f3.close()
f.close()
f1.close()
f2.close()