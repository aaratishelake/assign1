def word_count(str) :
     counts = dict()
     words = str.split()
     for word in words:
         if word in counts :
             counts[words] += 1
         else :
             counts[word] = 1
     return counts
f = open("aarti.txt","r")
message = f.read()
print(word_count(message))
with open('aarti.txt')as infile :
    lines=0
    words=0
    character=0
    for line in infile:
        wordlist=line.split()
        lines=lines+1
        words=words+len(wordlist)
print(lines)
print(words)