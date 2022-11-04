class user():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print("personal Details")
        print("")
        print("name",self.name)
        print("Age",self.age)
        print("Gender",self.gender)


class Bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("Account balance has updated: $",self.balance)

    def withdraw(self,amount):
        self.amount=amount
        if  self.amount>self.balance:
            print("Insufficient Funds|Balance Available:$",self.balance)
        else:
            self.balance=self.balance-self.amount
            print("Account balance has been updated:$",self.balance)
    def view_balance(self):
        self.show_details()
        print("Account balance:$",self.balance)
        
o1=Bank("vinay",22,"Male")
o1.deposit(1000)
o1.view_balance()
o1.withdraw(900)




