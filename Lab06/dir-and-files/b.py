import os
file_name = '/Users/esrarustemoglu/Desktop/Labs/Lab06/dir-and-files/a.txt'

print(os.access(file_name, os.F_OK))
print(os.access(file_name, os.R_OK))
print(os.access(file_name, os.W_OK))
print(os.access(file_name, os.X_OK))