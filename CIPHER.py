lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

encryptdict={}
decryptdict={}
rotation = int(input("What's the rotation size:"))

for l in range(0,len(lower)):
    rotator = l+rotation
    if rotator >= len(lower):
        rotator = rotator-len(lower)
    encryptdict.update({lower[l]:lower[rotator]})
    encryptdict.update({upper[l]:upper[rotator]})
    decryptdict.update({lower[rotator]:lower[l]})
    decryptdict.update({upper[rotator]:upper[l]})

def encryptor(string):
    string=list(string)
    temp=""
    for i in range(0,len(string)):
        if string[i] == " ":
            continue
        else:
            temp1 = encryptdict.get(string[i])
            string[i] = temp1
    print (temp.join(string))

def decryptor(string):
    string=list(string)
    temp=""
    for i in range(0,len(string)):
        if string[i] == " ":
            continue
        else:
            temp1 = decryptdict.get(string[i])
            string[i] = temp1
    print (temp.join(string))

print decryptor(string)
print encryptor(string)

