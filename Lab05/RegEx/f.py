import re
text = input()
pattern = ":"
result = re.sub(r"[ ,.]", pattern, text)
print(result)