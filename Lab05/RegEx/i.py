import re
text = input()
words = re.findall(r'[A-Z][a-z]*', text)
result = " ".join(words)
print(result)