import os
path = os.getcwd()
print(os.access(path, os.F_OK))
contents = os.listdir(path)
for x in contents:
    print(x)