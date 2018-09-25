# PROGRAMMING EXERCISE 2

# NUMBER 1

print("NUMBER 1")
x=[]
while(len(x))<3:
    num = input("input any number")
    x.append (num)
    print (x)
list.sort(x)
print("the max value is"+str(x[-1]))

print ("___________________________________")
print ("")

# NUMBER 2 :

print("NUMBER 2")
def stringLength(string):
    count = 0
    for i in string:
        count += 1
    return count
print(stringLength("Hello World"))

print ("___________________________________")
print ("")

# NUMBER 3 :

print ("NUMBER 3")
def stringVowel(letter):
    vowels=("a","e","i","o","u")
    if (letter in vowels):
        return True
    else:
        return False
print (stringVowel('b'))

print ("___________________________________")
print ("")

# NUMBER 4 :

print ("NUMBER 4")
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]

s = "eduj zenitram"
print (s)
print (reverse(s))

print ("___________________________________")
print ("")

# NUMBER 5

print ("NUMBER 5")
def is_member (x,a):
    for i in a:
        if i == x:
            print ("True")
            break
        else:
            print ("False")

is_member(8,[1,2,3])
print ("___________________________________")
print ("")

#NUMBER 6

print ("NUMBER 6")
def overlapping ():
    a=["a","b","c","d"]
    b=["q","w","e","r","t","y"]
    for i in a:
        for j in b:
            if i==j:
                return True
            else:
                return False

print (overlapping())

print ("___________________________________")
print ("")

#NUMBER 7

print("NUMBER 7")
def generate_n_chars(mult,chara):
    prnt = str()
    i=0
    for i in range (0,mult):
        prnt += chara
        print (prnt)



print ("___________________________________")
print ("")

#NUMBER 8

print("NUMBER 8")
def histogram(k):
    i=0
    for i in range (0,len(k)):
        print("k[i]")
histogram("1")

print ("___________________________________")
print ("")

#NUMBER 9

print("NUMBER 9")
def wordLength(s):
    i=0
    list = []
    for i in range (0,len(s)):
        list.append(len(s[i]))
    print(list)
wordLength("sleep")

print ("___________________________________")
print ("")

#NUMBER 10

print("NUMBER 10")
num=int(input("input number:"))
count=0
list=[]
while count<num:
    string=input("input word:")
    list.append(string)
    count+=1
list1=[]
def find_longest_word():
    for i in list:
        total=len(i)
        list1.append(total)
        if total==max(list1):
            a=max(list1)
        return a
print(find_longest_word())

print ("___________________________________")
print ("")

#NUMBER 11

print("NUMBER 11")
sentence =input("input sentence:")
def is pangram():
    c= 0
    alphabet = "abdefghijklmnopqrstuvwxyz"
    phraseletter = ""
    for char in sentence:
        for letter in alphabet:
            if char== letter and char not in phraseletters:
                phraseletter+= char
        for char in phraseletter:
            for letter in alphabet:
                if char==letter:
                    c+=1

        if c==26:
            return True
        else:
            print(phraseletter,alphabet)
            return False

print (is pangram())

print ("___________________________________")
print ("")

#NUMBER 12

print ("NUMBER 12")
word=input("Put some word:")
def make_ing_form():
    words=list(word)
    if words[-1]=='e'and words[-2]=="i":
        words=words[:2]
        words.append('ying')
        str1=".join(words)"
        print(str1)
    elif words[-1]=='e' and words[-2]!='i':
        words.append('ing')
        str1=".join(words)"
        print(str1)
    elif words[-2]=='a' or words[-2]=='i' or words[-2]=='u' or words[-2]=='e' or words[-2]=='o':
        if words[-1]!='a' or words[-1]!='i' or words[-1]!='u' or words[-1]!='e' or words [-1]!='o':
            if words[-3]=='a' or words[-3]=='i' or words[-3]=='u' or words[-3]=='e' or words[-3]=='o':
                words.append(word[-1])
                words.append('ing')
                str1 = ".join(words)"
                print(str1)
            else:
                words.append("ing")
                str1 = ".join(words)"
                return str1
        make_ing_form()
