import shelve as sv
import random
from src.customer import *
from src.Admin import *
from src.bank import *

def main(B1):
    print("""Enter :
        1 to Register
        2 to Login
        3 to Exit
        
        \t\tOr\n
        Enter pin to login in as Admin \"1826\" """)
    while True:
        button = int(input("\n=> ")) 

        #Creating a new account
        if button == 1:
            B1.register()
            print("...")

        #Logging in as a User
        elif button == 2:
            B1.logIn()

        #Logging in as Admin    
        elif button == adminPin:
            control = Admin()
            while True:
                control.menu()
                if control.options == 1:
                    control.viewUsers()

                elif control.options == 2:
                    control.searchUser()

                elif control.options == 3:
                    control.logOut()
                    break

                else:
                    print("\tUnknown..")

        #Logging Out
        elif button == 3:
            print("\n\tThanks for checking out my program!")
            return None

        else:
            print("aNot recognized")
        """except:
            print("bNot recognized")"""

if __name__ == "__main__":
    adminPin = 1826
    B1 = Bank("Guarantee trust bank")
    main(B1)
