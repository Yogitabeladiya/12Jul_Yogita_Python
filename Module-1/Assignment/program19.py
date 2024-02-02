#find the lonest one 
n=input("enter string")
longest=0
for words in n.split():
    if len(words)<longest:
        longest=len(words)
       # longest_word=words
print("lonest word is",words,"with length",len(words))
