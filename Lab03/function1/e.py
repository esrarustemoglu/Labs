def perm(string, i = 0):
    if i == len(string):
        print ("".join(string))
    for j in range (i, len(string)):
        word = [x for x in string]
        word[i], word[j] = word[j], word[i]
        perm(word, i + 1)
print(perm("abc"))