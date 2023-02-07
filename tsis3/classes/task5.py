class Account:
    def __init__(self,name):
        self.name=name
        self.dep=0

    def owner(self):
        print(f"owner of accaunt is:{self.name}")

    def deposit(self,give):
        self.dep+=give
        print(f"you deposited {self.dep} dollars")
    
    def balance(self):
        print(f"you heve {self.dep} dollars")
    
    def withdraw(self,take):
        self.take=take
        if self.take <=self.dep:
            self.dep-=self.take
            print("take your money")
        else:
            print("your deposite lower than needed money")

depos1=Account("hell")
depos1.owner()
depos1.deposit(20)
depos1.balance()
depos1.deposit(20)
depos1.balance()
depos1.withdraw(38)
depos1.balance()
depos1.withdraw(4)
depos2=Account("heaven")
depos2.owner()
depos2.deposit(22)
depos2.balance()
depos2.deposit(234)
depos2.balance()
depos2.withdraw(345)
depos2.balance()
depos2.withdraw(45)
