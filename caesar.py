f=open("input.txt","r")
fk=open("key.txt","r")
fo=open("output.txt","w")
for key in fk:
    key=int(key)
key=key%26
output=""
for each in f:
    for i in each:
        if(i.isupper()):
            temp=chr((ord(i)+key-65)%26+65)
            output+=temp
        elif(i.islower()):
            temp=chr((ord(i)+key-97)%26+97)
            output+=temp
        else:
            output+=i
fo.write(output)

fd=open("decrypt.txt","w")
#for k in range(0,26):
result=""
for i in output:
    if(i.isupper()):
        temp=chr((ord(i)+26-key-65)%26+65)
        result+=temp
    elif(i.islower()):
        temp=chr((ord(i)+26-key-97)%26+97)
        result+=temp
    else:
        result+=i
fd.write(result)

fk.close()
f.close()
fo.close()
fd.close()
print(fo)