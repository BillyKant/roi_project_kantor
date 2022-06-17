class User_Mixin():

    def create_user(self):
            

            # While loop used to determine if user name already exists, creates user data library if unique user_name given
            while True:
                user = input('\nUser Name: ')
                if user not in self.users:
                    self.users[user] = {}
                    self.users[user]['user_name'] = user
                    self.user = user  # todo: temporary var to allow code to run
                    break
                else:
                    print('\nThis User Name already exists, please choose another')

            pass_w = input('\nPassword: ')
            self.users[user]['password'] = pass_w

            first = input('\nFirst Name: ')
            self.users[user]['first_name'] = first

            last = input('\nLast Name: ')
            self.users[user]['last_name'] = last

            email = input('\nEmail: ')
            self.users[user]['email'] = email 

            phone = input('\nPhone Number: ')
            self.users[user]['phone_num'] = phone 
            print(self.users)




class ROI_Calculator(User_Mixin):

    def __init__(self):
        self.users = {}
        self.user = '' # todo temp var to allow code to run
        self.prop = ''


    # Method to run program
    def start(self):
        print("""
    --- Welcome to the KANT-RENT ROI Calculator ----

        - What would you like to do? -

            [1] Login
            [2] Sign-Up

        """)

        #Sign In or Sign Up
        
        while True:

            action1 = input('\nInput here: ')

            # Sign in 
            if action1 == '1':
                while True:
                    user_id = input('\nUser Name: ') 
                    if user_id in self.users:
                        break
                    else:
                        question = input("\n We don't recognize this user name, would you like to create an account ('y' or 'n')?")
                        if question == 'y':
                            self.create_user()
                        # else:
                        #     pass
                

                while True:
                    pass_in = input('\nPassword: ')
                    if pass_in == self.users[user_id]['password']:
                        break
                    else:
                        print('\nIncorrect password, please try again...')
                break
            # todo: add other methods to continue program (maybe put sign-in/sign-up in it's own method? maybe make it part of User_Mixin?)
            #Sign up
            elif action1 == '2':
                self.create_user()
                print("""
        - What would you like to do? -

            [1] Login
            [2] Sign-Up

        """)

            elif action1 == 'q':
                break # todo: add a way to exit program completely
                
            else:
                print('\nDoes not recognize input, please try again.')

        print(f"\nWelcome back {user_id}!")

        self.menu()

    # Method for main menu   
    def menu(self):

        print("""\n
    --- What would you like to do? ---

        [1] Add a new Property
        [2] See my properties 
        [3] Change a property's info
        [4] Switch User

        """)
        selection = input('\nInput: ')
        if selection == '1':
            self.new_property()



    # Method to create a new property
    def new_property(self):
        
        while True:
            prop = input('\nStreet Address: ')
            if prop not in self.users[self.user]:            # ! How do I access a user created in mixin and then input in class method
                self.users[self.user][prop] = {}         # todo: need to adjust user variable
                self.users[self.user][prop]['street address'] = prop 
                self.prop = prop
                break
            else:
                print('\nThis property already exists, please choose another')

        city = input('\nCity: ')
        self.users[self.user][self.prop]['city'] = city
        state = input('State: ')
        self.users[self.user][self.prop]['state'] = state
        zip = input('Zip code: ')
        self.users[self.user][self.prop]['zip'] = zip

        self.roi_info()

    

    def roi_info(self):
        income_lst = ['rent','laundry','storage']
        expenses_lst = ['mortgage','taxes','utilities','vacancy','repairs','capEx']
        self.users[self.user][self.prop]['roi'] = {}

        #Income
        print("\nPlease tell us about the monthly income this property will generate.")
        # Create library to store incomes
        self.users[self.user][self.prop]['roi']['income'] = {}

        while True:
            #While loop to allow user to add incomes
            print(income_lst) 
            incomes = input("\nPlease enter an expense you would like to add from the list (enter 'q' to quit): ")
            if incomes in income_lst:
                amount = int(input("\nHow much will this be per month?: "))
                self.users[self.user][self.prop]['roi']['income'][incomes] = amount
            elif incomes == 'q':
                break
            else:
                print('\nDoes not recognize input, please try again.')

        # Sum all income values for total
        
        k = self.users[self.user][self.prop]['roi']['income']
        summation = sum(k.values())       
        
        self.users[self.user][self.prop]['roi']['income']['total'] = summation
        print(self.users[self.user][self.prop]['roi']['income'])
        print(self.users[self.user][self.prop]['roi']['income']['total'])
        print(self.users)

        # rent = input('Rent: ')
        # self.users[self.user][self.prop]['roi']['income']['rent'] = int(rent)

        # laundry_q = input("Is there a laundry? ('y' or 'n'): ")
        # if laundry_q == 'y':
        #     laundry = input('Laundry: ')
        #     self.users[self.user][self.prop]['roi']['income']['laundry'] = int(laundry)
        # storage_q = input("Is there storage? ('y' or 'n'): ")
        # if storage_q == 'y':
        #     storage = input('Storage: ')
        #     self.users[self.user][self.prop]['roi']['income']['storage'] = int(storage)

        # self.users[self.user][self.prop]['roi']['income']['value'] = int(rent) + int(laundry) + int(storage)  # ! if I don't have cost in a category this does not work
        

        #Expenses
        print("\nPlease tell us about the monthly expenses that this property will incur.")
        self.users[self.user][self.prop]['roi']['expenses'] = {}
        mortgage = input('Mortgage: ')
        self.users[self.user][self.prop]['roi']['expenses']['mortgage'] = int(mortgage)
        tax = input('Taxes: ')
        self.users[self.user][self.prop]['roi']['expenses']['taxes'] = int(tax)
        utilities = input('Utilities: ')
        self.users[self.user][self.prop]['roi']['expenses']['utilities'] = int(utilities)
        vacancy = input('Vacancy: ')
        self.users[self.user][self.prop]['roi']['expenses']['vacancy'] = int(vacancy)
        repairs = input('Repairs: ')
        self.users[self.user][self.prop]['roi']['expenses']['repairs'] = int(repairs)
        capEx = input('capEx: ')
        self.users[self.user][self.prop]['roi']['expenses']['capEx'] = int(capEx)

        manager_q = input("Is there a property manager? ('y' or 'n'): ")
        if manager_q == 'y':
            manager = input('Manager: ')
            self.users[self.user][self.prop]['roi']['expenses']['manager'] = int(manager)
        hoa_q = input("Is there a laundry? ('y' or 'n'): ")
        if hoa_q == 'y':
            hoa = input('HOA: ')
            self.users[self.user][self.prop]['roi']['expenses']['hoa'] = int(hoa)

        self.users[self.user][self.prop]['roi']['expenses']['value'] = int(mortgage) + int(tax) + int(utilities) + int(vacancy) + int(repairs) + int(capEx) + int(manager) + int(hoa) # ! if I don't have cost in a category this does not work
    

        # self.menu()



    def test_dict(self):
        print(self.users)


test1 = ROI_Calculator()

test1.start()

test1.test_dict()

