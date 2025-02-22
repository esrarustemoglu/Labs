import re
text = input()
pattern = "[a-z]"
result = re.findall(pattern, text)
result = "_".join(result)
print(result)