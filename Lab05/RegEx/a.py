import re
text = input()
pattern = "^ab*$"
result = re.match(pattern, text)
print(result) 
print(result.group(0)) 