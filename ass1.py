def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


f = open("aarti.txt", "r")
message = f.read()

print(word_count(message))