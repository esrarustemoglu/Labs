import re
text = input()
lst = list(text)  
for i in range(len(lst) - 1):  
    if lst[i] == "_":
        lst[i + 1] = lst[i + 1].upper() 

text  = "".join(lst)  
result = re.sub("_", "", text)  
print(result)