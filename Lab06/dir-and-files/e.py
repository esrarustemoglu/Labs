import json
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
file_name = '/Users/esrarustemoglu/Desktop/Labs/Lab06/dir-and-files/a.txt'
with open(file_name, 'w') as file:
    a = json.dump(l, file)
