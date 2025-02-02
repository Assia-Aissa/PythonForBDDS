import random 
class compte:
    #static attribute 
    nbr_accounts=0
    def __init__(self,soldeInitial,ClientName,adress="casa"):
        print("hi i'm the constructor of the class")
        # initialisation of the attributes
        self.__solde=soldeInitial
        self.__name=ClientName
        self.__numAccount=random.random()
        self.__adress=adress
        self.__class__.nbr_accounts+=1
    # methodes
    def GetSold(self):
        return self.__solde
    def Deposit(self,amount):
        self.__solde+=amount
    def __del__(self):
        print("the account of "+self.__name+" has been deleted")
        self.__class__.nbr_accounts-=1
    def Display(self):
        print(f"the client {self.__name}have :{self.__solde}in his account")
    @classmethod
    def Number_of_accounts(cls):
        print("At this time the number of account is :"+__class__.nbr_accounts)
    def Undeposit(self,amount):
        if self.__solde>amount:
            self.__solde -=amount
        else:
            print("impossible yout account does not have even this amount of money to take it are u stupid haaaaah ")
    def Transfer(self,amount,account):
        if self.__solde>amount:
            self.__solde -=amount
            account.Deposite(amount)
        else:
            print("u do not have that much money to transfer poor client  ")

account1=compte(1000,"mohamed")
account2=compte(500,"youssef")
account1.Display()
account2.Display()
account1.GetSold()
account2.GetSold()


