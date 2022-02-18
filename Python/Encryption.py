resultE=''
message=''
resultD=''
message=input("\nEnter the message to encrypt: ")
for i in range(0,len(message)):
    resultE=resultE+chr(ord(message[i])-2)
print("Encrypted Message:",resultE)

for j in range(0,len(resultE)):
    resultD=resultD+chr(ord(resultE[j])+2)
print("Decrypted Message:",resultD)
