class Something:
    def __init__(self):
        self.string=''
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string)
someString=Something()
someString.getString()
someString.printString()
