#bank management

class bank:
    def __init__(self,deposit):
        print("Account created")
        self.deposit=deposit
    
        
    def new_deposit(self,new):
        
    
        self.deposit+=new
        return self.deposit
    
    def withdrawal(self,withdrawal):

        self.deposit-=withdrawal
        
        return self.deposit
    def balance(self):


        print(f"remaining balance={self.deposit}")
        return self.deposit

customer1=bank(1000)
while True:
    choice=int(input("Enter your choice:\n1.New deposit,2.Withdrawal,3.Check balance,4.Exit"))
    if choice==1:
        amount=int(input("Enter the amount to be deposited:"))
        customer1.new_deposit(amount)
        print("Amount deposited")
    elif choice==2:
        withdraw=int(input("Enter the amount to be withdrawn:"))
        if withdraw> customer1.deposit:
            print("Insufficient amount")
        else:
            customer1.withdrawal(withdraw)
            print("Successffully withdrawn")
    elif choice==3:
        customer1.balance()
    elif choice==4:
            print("Thank you")
            break
    

        


                     
    
    
    

