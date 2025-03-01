file_name = '/Users/esrarustemoglu/Desktop/Labs/Lab06/dir-and-files/a.txt'
file_1_name = '/Users/esrarustemoglu/Desktop/Labs/Lab06/dir-and-files/d.txt'
with open(file_name, 'r') as file, open(file_1_name, 'a') as file_1:
    file_1.write(file.read())