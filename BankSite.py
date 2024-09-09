# Bank Management system
# import random
import time
from abc import ABC
class CustomerDetails(ABC):
    __CustomerCount=0 
    BankName="State Bank Of India"
    Ifc_Code="SBI000000101"
    BankBranch="vijayNagar,Indore"
    def __init__(self,CN,CAge,Cdob,PassW):
        # self.UserId=random.choice()
        self.CustomerName=CN
        self.CustomerAge=CAge
        self.CustomerDOB=Cdob
        self._Password=PassW
        CustomerDetails.Successfull()
        CustomerDetails.__CustomerCount=CustomerDetails.__CustomerCount+1

    @staticmethod
    def Welcomemessage():
        print("------------WELCOME TO SBI------------- ")
        print("---------STATE BANK OF INDIA---------- ")
    
    @staticmethod
    def Successfull():
        print("You Have successfully Created An account!")
    def Password(self):
        password=input("Enter Your Password")
        self._Password=password
    
    def __UpdatePassword(self):
        print("Enter Your Old Password\n")
        password=input()
        if password==self._Password:
            self._Password=password
        # make this to check the old password if correct then procceed otherwise throw new error

class Account(CustomerDetails):
    def __init__(self,CN,CAGE,CDOB,PassW):
        super().__init__(CN,CAGE,CDOB,PassW)
        self.__Balance=''
        self.__UpdateBalance()
    def __UpdateBalance(self):
        Balance=int(input("Enter The Amount:"))
        print("Please Wait....Your query is processing")
        time.sleep(3)
        self.__Balance=Balance
        print("Your Amount Successfully Updated!")
        
    def Credit(self):
        password=input("Enter Your Amount:")
        if self._Password==password:
            Amount=input("Enter Your Amount")
            self.Balance+=Amount
            print("Your money is deposite!")
        else:
            print("Your Password Is Incorrect !")
    def Debit(self):
        password=input("Enter YOur Password")
        if self._Password==password:
            Amount=input("Enter Your Amount")
            if Amount<=self.Balance:
                self.Balance=self.Balance-Amount
                print('Take Your Case')
                print("Your Remainig amount is:",self.Balance)
        
                self.Balance+=Amount
                print("Your money is deposite!")
            else:
                print("You have not sufficient balance")
        else:
            print("Your Password Is Incorrect !")

    def showbalance(self, Balance):
        self.__Balance()
        print( self.__Balance)
    def Inquiry(self):
        pass
        # print("user")complete The Function

while(True):
    CustomerDetails.Welcomemessage()
    print("What Do You Want:\n Press:1 For New Account,\n Press:2 Already Have an Account")
    Coice=int(input())
    if(Coice==1):
        username=input("Enter Your Name: ")

        Age=int(input("Enter Your Age: "))
        if Age>=18:
            pass
        else:
            print("You are not elegible!")
            break

        Dob=input("Enter Your Dob: ")
        print("(Password must contain alphabate,uppercasecharacter,number)")
        PassW=input("Enter Your  Password: ")
        customer1=Account(username,Age,Dob,PassW)

        continue
    elif Coice==2:
        print("\nPress1: For Checking Your Balance\nPress2: For Credit Amount\nPress3: For Debit Amount\nPress4: For Inquiry")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            int(customer1.showbalance())
            print("Your Balance Is: ", customer1.showbalance)
            continue
        elif choice==2:
            credit=int(input("Enter your credit amount: "))
            print(f"Amount of {credit}rs is crediting in your account")
            break
    else:
        print("Invalid Input !")
        break



        



# press 4 for enquiry all details of customer

# customer1.showbalance(10000)

# while True:
    
    # make forward this code
# customer create
    # userName,Age,Dob
    # check the age is eligible or not 
    # Password
# credit amount by user
# welcome message print
# terms and condition print 
#Choice 1,2,3,4
    # 1 for Check Your Balance
    # 2 for  Credit
    # 3 for debit
    # 4 for Inquiry,name,age,dob,blance,bankdetails
    