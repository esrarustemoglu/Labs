import os
if os.path.exists("h.txt"):
    os.remove("h.txt")
else:
    print("The file does not exists")