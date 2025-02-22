import re
text = input()
pattern = "^ab{2,3}$"
result = re.match(pattern, text)
print(result) 
print(result.group(0)) 