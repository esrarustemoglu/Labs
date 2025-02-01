def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    print(' '.join(words))
string = input()
reverse_words(string)