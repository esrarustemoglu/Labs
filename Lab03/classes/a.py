class string:
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
sentence = string()
sentence.getString()
sentence.printString()