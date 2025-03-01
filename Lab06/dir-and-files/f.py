import os
directory = "/Users/esrarustemoglu/Desktop/Labs/Lab06/dir-and-files/"
for ascii_value in range(65, 91):  
    letter = chr(ascii_value)  
    file_name = os.path.join(directory, f"{letter}.txt")
    with open(file_name, 'w') as file:
        file.write(f"This is file {letter}.txt\n")