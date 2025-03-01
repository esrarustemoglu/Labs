file_name = '/Users/esrarustemoglu/Desktop/Labs/Lab06/dir-and-files/d_1.txt'
line_count = 0
with open (file_name, 'w')as file:
    file.write("hello \neveryone \n123 \nabc")
with open(file_name, 'r') as file:
    for line in file:
        line_count += 1
    print(line_count)