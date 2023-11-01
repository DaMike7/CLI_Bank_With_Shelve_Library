import shelve as sv

class Admin():
    def __init__(self):
        self.Namelist = list()
        self.options = str()

        with open("src/db/customers.txt") as f:
            for lines in f:
                names = str(lines.strip()) 
                self.Namelist.append(names)

    def menu(self):
        print(f"\n\tGuarantee TrustBank Administration\n")
        print("""
        Enter :
        1  to see view users
        2  to search for a user
        3  to log out
        """)
        try:
            options = int(input("\t- "))
            self.options = options

        except:
            print("\n\t*numeric prompts only!")

    def viewUsers(self):
        print()
        print("\tProcessing....\n")

        for N,Names in enumerate(self.Namelist,start=1):
            print(f"\t{N}. {Names}")
        print('\n\n')
        print(f'\tTotal : {len(self.Namelist)} active user(s) !')
        print('..'*30)

    def searchUser(self):
        print("\n\tProcessing....\n\t*click \"ENTER\" anytime to exit.....\n")
        while True:
            name = input("\n\tEnter Customer\'s Name Below\n\t- ")
            if name in self.Namelist:
                try:
                    User = sv.open(f"src/db/{name}")
                except:
                    print("\n\tAn unexpected error occured!")
                else:
                    print("\n\tprocessing...\n")
                    print('\tId','  ','Name','   ','Age','  ','EmailAddress','     ','Balance','     ','Pin ')
                    print("\t",User["Id"]," ",User["Name"],"     ",User["Age"],"   ",User["EmailAddress"],"      ",User["Balance"],"     ",User["Pin"]," \n")
                    User.close()
            elif name == "":
                print("\n\t\tExiting....\n")
                print('..'*30)
                return

            else:
                print(f"\n\tName \"{name}\" not found!")


    def logOut(self):
        print("\n\tLogging Out...")
        print('..'*30)
        return
