import shelve as sv
import random as r
import json
import re
from .customer import *
from .Admin import *

with open("src/db/id.json","r") as f:
    _id = json.load(f)
last_id = _id

class Bank:
    def __init__(self,bankName):
        self.bankName = bankName
        self.user = str()
        self.cname = str()
        self.cAge = int()
        self.cId = int()
        self.cBal = 400.0
        self.cEmail = str()

    def register(self):
        global last_id
        from .customer import Customer
        for a in range(2):
            self.cname = input("\nWhat is your name ")
            Me = Admin()
            if self.cname == "":
                print("\n*Can't leave name field blank!")

            elif self.cname not in Me.Namelist:
                for b in range(2):
                    try:
                        self.cAge = int(input("\nEnter age "))
                    except:
                        print("\ndigits only!")
                    else:
                        if not 18<= self.cAge <= 70:
                            print("\nMust be 18 and older, Must not be older than 70")
                        else:
                            print()
                            for c in range(2):
                                emailAddress = input("\nEnter your email address ")
                                eRgx = re.compile(r"""(
                                [a-zA-Z0-9.-]+   #username
                                @                #@ symbol
                                [a-zA-Z0-9.-]+   #domain name
                                (\.[a-zA-Z]{2,4}) #dot-something
                                )""",re.VERBOSE)

                                self.cEmail = eRgx.search(emailAddress)

                                if self.cEmail:
                                    for d in range(2):
                                        try:
                                            self.cPin = int(input("\nCreate a 4-digit password\n"))
                                        except:
                                            print("\nPassword must be digits only")
                                        else:
                                            if not len(str(self.cPin)) == 4:
                                                print(f"\nit must be a 4-digit password\nyou have {d} chance(s) left!")

                                            else:
                                                cEmail = str(self.cEmail)
                                                last_id += 1
                                                self.cId = last_id 
                                                self.user = Customer(self.cId,self.cname,emailAddress,self.cAge,self.cPin,self.cBal)

                                                with open("src/db/id.json","w+") as f:
                                                    json.dump(self.cId,f)

                                                with open(f"src/db/customers.txt","a+") as cs:
                                                    cs.write(f"{str(self.cname)}\n")
                                                
                                                customer = sv.open(f"src/db/{self.cname}")
                                                customer["Id"] = self.user.id
                                                customer["Name"] = self.user.Name
                                                customer["EmailAddress"] = self.user.Email
                                                customer["Age"] = self.user.Age
                                                customer["Pin"] = self.user.Pin
                                                customer["Balance"] = self.user.Balance

                                                customer.close()

                                                print(self.user.id)
                                                return None

                                else:
                                    print(f"\ninvalid email address\nyou have {c} chances left!")
            else:
                print("\nInvalid Name or Name Already exists! ")

    def logIn(self):
        from .customer import Customer
        print("\n\tProcessing.....\n\tclick \'ENTER\" anytime to exit\n\t...")
        while True:
            Username = input("\n\tEnter your username ")
            Me = Admin()
            if Username in Me.Namelist: 
                for Try in range(2):
                    try:
                        Password = int(input("\n\tEnter your pin to log in :  "))
                    except:
                        print("\t*digits only\n you have 0 chances left")
                    else:
                        CUSTOMER = sv.open(f"src/db/{Username}")
                        if not Password == CUSTOMER["Pin"]:
                            print("\n\t*incorrect!\n\tyou have 0 chances left")
                        else:
                            print(f"\n\tWelcome {Username.title()}! ....")
                            self.CUSTOMER = CUSTOMER
                            for a in range(2):
                                try:
                                    otp = r.randint(4519,7899)
                                    authenticate = int(input(f"\n\tAlmost there \"{otp}\"\n\tEnter otp\n\t.. "))

                                except:
                                    print(f"\n\tdigits only")

                                else:
                                    if not authenticate == otp:
                                        print(f"\n\t\tincorrect\n\tyou have {a} chance(s) left!")
                                    else:
                                        print()
                                        while True:
                                            print("""\n\tEnter :
                    1 to deposit
                    2 to withdraw
                    3 to request for account statement
                    4 to check balance
                    5 to log out""")
                                            try:
                                                self.user = Customer(self.CUSTOMER['Id'],self.CUSTOMER['Name'],self.CUSTOMER['EmailAddress'],self.CUSTOMER['Age'],self.CUSTOMER['Pin'],self.CUSTOMER['Balance'])
                                                button = int(input("\n\t\t-> "))
                                            except:
                                                print("\nInvalid!")

                                            else:
                                                if button == 5:
                                                    print("\n\t\t...Logging out")
                                                    return

                                                elif button == 1:
                                                    self.user.deposit()

                                                elif button == 2:
                                                    self.user.withdraw()

                                                elif button == 3:
                                                    self.user.viewInfo()

                                                elif button == 4:
                                                    self.user.viewBalance()

            elif Username == "":
                return

            else:
                print(f"\t\"{Username}\" not found!!")

        self.CUSTOMER.close()
