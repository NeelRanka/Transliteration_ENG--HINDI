#problem for half words solved
import dill
import sys

file = open(input('path to the pkl file '),'rb')
obj = dill.load(file)
file.close()

phdict = obj.HI_to_Ph
vowel = obj.vowels
consonent = obj.consonents
rev = obj.Ph_to_EN


test_str=""
#var=input("enter the file name(with extension) ")

file=open(sys.argv[1],"r",encoding="utf-8")
for line in file:                                #to take a file input
    for ch in line:
        test_str+=ch
#test_str=input("enter a name in hindi ")       #to take idle input

temp = list(test_str)

op_string=[]
    


for x in range (0,len(temp)-1):
    if temp[x] in phdict:
        op_string.append(phdict[temp[x]])
        if temp[x] not in vowel and (temp[x+1] not in vowel and temp[x+1] != ' ' and temp[x+1] != '.') :
        	op_string.append("ah")

    elif temp[x]==' ' or temp[x] == '.' or temp[x] in [' ', '.', ',', '\n', '\t'] :
        op_string.append(temp[x])

        
if temp[-1] in phdict:
    op_string.append(phdict[temp[-1]])

v=['a','e','i','o','u']

while '' in op_string : op_string.remove('')

print(op_string)
final_str=""


for i in range(0,len(op_string)-1):
    if op_string[i]==' ':
        final_str+=' '
    else:
        if op_string[i]=='n' and i!=0:
            if op_string[i]=='n' :
                if final_str[-1] not in v and final_str[-1]!=op_string[i] and final_str[-1]!=' ':
                    final_str+='an'
                else:
                    final_str+='n'
                               #for special case of ं
            else:
                final_str+='n'
        else:    
            if op_string[i] in rev:
                final_str+=rev[op_string[i]]
            
if op_string[-1] in rev:
    final_str+=rev[op_string[-1]]
 
###########################################################################
#correction part

#findword={}

# Below is an old code for correction of the transliterated text.
# Go ahead and make a dictionary for correction of the text and maybe store it in a file or add it in the .pkl file

"""
def makedict():#to make a dict of correction file
    file=open("correction.txt","r")
    for line in file:
        line=line.split()
        if line[0] not in findword:
            findword[line[0]]=line[1]
    file.close()            
"""

#final_str=final_str.split()  #final output string in list form

#makedict()
"""
for i in range(0,len(final_str)):
    if final_str[i] in findword:
        final_str[i]=findword[final_str[i]]
"""        
#final_str=" ".join(final_str)

print("\n\n",final_str)

"""
while 1:
    ask=input("do you want a correction(y/n) ")
    if ask=="\r" or ask=="\n" or ask=='':
        continue
    if ask=='n':
        break
    if ask=='y':
        which=input("which word do you want corrected ")
        final_str=final_str.split()
        if which in final_str:
            if which in findword:
                for x in range(0,len(final_str)):
                    if final_str[x]==which:
                        final_str[x]=findword[which]
            else:        
                word=input("enter the corrected word ")
                file=open("correction.txt","a")
                file.write(which)
                file.write("\t")
                file.write(word)
                file.write("\n")
                for x in range(0,len(final_str)):
                    if final_str[x]==which:
                        final_str[x]=word
        else:
            print("word not found ")
    else:
        print("enter a valid choice ")
        continue
    
    file.close()
    final_str=" ".join(final_str)
    print(final_str)
"""
