import re
text = "I Dont Know"
pattern = "[A-Z]"
pattern_1 = "[a-z]"
x = re.findall(pattern, text)
x_1 = re.findall(pattern_1, text)
print(f"Upper case letters :{len(x)}")
print(f"Lower case letters :{len(x_1)}")