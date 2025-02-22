import re
text = input()
words = re.findall(r'[A-Z][a-z]*', text)
result = "_".join(words)
result = result.lower()
print(result)