from .bank import *

class Customer:
    def __init__(self,id,Name,Email,Age,Pin,Balance):
        self.Name = Name
        self.Age = Age
        self.Email = Email
        self.Pin = Pin
        self.id = id
        self.Balance = Balance

    def deposit(self):
        print()
        try:
            amt = int(input("""
                Max deposit : N500,000
                Min deposit : N500
                """))
        except:
            print("\tdigits only!")
        else:
            if 500 <= amt <= 500_000 :
                for a in range(2):
                    try:
                        pin = int(input('\n\t\tEnter pin to confirm deposit '))

                    except:
                        print("\n*digits only")
                    else:
                        if pin == self.Pin:
                            self.Balance += float(amt)
                            print(f"\n\t\tsuccessful!\n\t\tBalance : N{self.Balance}")

                        else:
                            print("\t\t*incorrect!")
                            return

            else:
                print("""\t\tAmount must be more than N500 and less than N500""")

    def withdraw(self):
        print()
        try:
            amt = int(input("""
    Max withdrawal : N200,000
    Min wothdrawal : N1000
    """))
        
        except:
            print("\ndigits only!")
        else:
            if 1000 <= amt <= 200_000:
                if not self.Balance <= float(amt) >= self.Balance:
                    for a in range(2):
                        try:
                            pin = int(input('\n\tEnter pin to confirm withrawal '))
    
                        except:
                            print("\n*digits only")
                        else:
                            if pin == self.Pin:
                                self.Balance -= float(amt)
                                print(f"""
                                successful
                                \nBalance : N{self.Balance}
                                """)

                            else:
                                print("*incorrect!")

                else:
                    print("\ninsufficient balance!")
                    
            else:
                print("Can\'t withraw more than N200,000 or less than N100")

    def viewInfo(self):
        print()
        for a in range(2):
            try:
                Pass = int(input('\t\tEnter Pin to Continue\n\t\t  '))
            except:
                print("\t\t*error!\n\t\tEnter Pin!")
            else:
                if not Pass == self.Pin:
                    print('\t\t*Incorrect!\n\t\tyou have 0 chances left')

                else:
                    print("\t\tprocessing...")
                    print()
                    print('\t\tName','   ','Age','     ','EmailAddress','       ','Balance','     ','Pin ')
                    print(f'\t\t{self.Name}','   ',f'{self.Age}','     ',f'{self.Email}','       ',f'{self.Balance}','     ',f'{self.Pin} ')
                    print()
                    return
                return

    def viewBalance(self):
        print()
        for a in range(2):
            try:
                Pass = int(input('\t\tEnter Pin to Continue\n\t\t  '))
            except:
                print("\t\t*error!\n\t\tEnter Pin!")
            else:
                if not Pass == self.Pin:
                    print('\t\t*Incorrect!\n\t\tyou have 0 chances left')

                else:
                    print("\t\tprocessing...")
                    print()
                    print(f'\t\tBalance : {self.Balance}')
                    return
                return
