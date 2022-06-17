class User_Mixin():

    def create_user(self):
            

            # While loop used to determine if user name already exists, creates user data library if unique user_name given
            while True:
                user = input('\nUser Name: ')
                if user not in self.users:
                    self.users[user] = {}
                    self.users[user]['user_name'] = user
                    self.user = user  
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
            print(f'\n{self.users}')




class ROI_Calculator(User_Mixin):

    def __init__(self):
        self.users = {}
        self.user = {} 
        self.prop = {}
        self.data_flag = True


    # ***Method to run program***
    def start(self):
        print("""\n
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
            # Sign up
            elif action1 == '2':
                self.create_user()
                print("""\n
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

    # ***Method for main menu***   
    def menu(self):

        while True:
            print("""\n
    --- What would you like to do? ---

        [1] Add a new Property
        [2] See my information
        [3] Change ROI data
        [4] Switch User
        [5] Quit

        """)
            selection = input('\nInput: ')
            if selection == '1':
                self.new_property()
            elif selection == '2':
                if self.prop != {}:      
                    print(f'\n{self.users[self.user]}')  
                else:
                    print("\nYou don't have any properties yet.")
            elif selection == '3':
                self.change_data()
            elif selection == '4':
                self.start()
            elif selection == '5':
                break



    # ***Method to create a new property***
    def new_property(self):
        
        if self.data_flag == True:
            while True:
                prop = input('\nStreet Address: ')
                if prop not in self.users[self.user]:            
                    self.users[self.user][prop] = {}         
                    self.users[self.user][prop]['street address'] = prop 
                    self.prop = prop
                    break
                else:
                    print('\nThis property already exists, please choose another')

        else:
            prop = input('\nWhat property would you ')

        city = input('\nCity: ')
        self.users[self.user][self.prop]['city'] = city
        state = input('\nState: ')
        self.users[self.user][self.prop]['state'] = state
        zip = input('\nZip code: ')
        self.users[self.user][self.prop]['zip'] = zip

        self.roi_info()

    

    def roi_info(self):
        income_lst = ['rent','laundry','storage','other']
        expense_lst = ['mortgage','taxes','insurance','utilities','vacancy','repairs','capEx','manager','hoa','other']
        cash_on_cash_lst = ['down payment','closing costs','rehab budget','other']
        


        # ***Income***
        if self.data_flag == True:  # !
            self.users[self.user][self.prop]['roi'] = {}
            print("\nTell us about the monthly income this property will generate.")
            # Create library to store incomes
            self.users[self.user][self.prop]['roi']['income'] = {}

        while True:
            # While True loop to allow user to add income categories and assign values
            print(f'\n{income_lst}') 
            if self.data_flag == True: # !
                incomes = input("\nPlease enter an income you would like to add from the list (enter 'q' to quit)?: ")
            else:                       # !
                incomes = input("\nWhich incomes from the list would you like to add or change (enter 'q' to quit)?: ")
            if incomes in income_lst: 
                amount = int(input("\nHow much will this be per month?: "))
                self.users[self.user][self.prop]['roi']['income'][incomes] = amount
            elif incomes == 'q':
                break
            else:
                print('\nDoes not recognize input, please try again.')

        # Sum all income values for total
        k = self.users[self.user][self.prop]['roi']['income']
        summation_i = sum(k.values())       
        self.users[self.user][self.prop]['roi']['income']['total'] = summation_i


        # ***Expenses***
        print("\nTell us about the monthly expenses that this property will incur.")
        # Create library to store incomes
        self.users[self.user][self.prop]['roi']['expense'] = {}

        while True:
            # While True loop to allow user to add income categories and assign values
            print(f'\n{expense_lst}') 
            if self.data_flag == True:
                expenses = input("\nPlease enter an expense you would like to add from the list (enter 'q' to quit): ")
            else:
                expenses = input("\nWhich expenses from the list would you like to add or change (enter 'q' to quit)?: ")
            if expenses in expense_lst:
                amount = int(input("\nHow much will this be per month?: "))
                self.users[self.user][self.prop]['roi']['expense'][expenses] = amount
            elif expenses == 'q':
                break
            else:
                print('\nDoes not recognize input, please try again.')

        # Sum all expense values for total
        k = self.users[self.user][self.prop]['roi']['expense']
        summation_e = sum(k.values())       
        self.users[self.user][self.prop]['roi']['expense']['total'] = summation_e


        # ***Cash Flow***
        self.users[self.user][self.prop]['roi']['monthly cash flow'] = summation_i - summation_e
        cash_flow = self.users[self.user][self.prop]['roi']['monthly cash flow']
        print(f"\nYour cash flow is {cash_flow}")


        # ***Cash on Cash ROI***
        print("\nTell us about the expenses you put into purchasing and preparing the property.")
        # Create library to store incomes
        self.users[self.user][self.prop]['roi']['cash on cash'] = {}

        while True:
            # While True loop to allow user to add income categories and assign values
            print(f'\n{cash_on_cash_lst}') 
            if self.data_flag == True:
                initial_expenses = input("\nPlease enter an expense you would like to add from the list (enter 'q' to quit): ")
            else:
                initial_expenses = input("\nWhich expenses from the list would you like to add or change (enter 'q' to quit)?: ")
            if initial_expenses in cash_on_cash_lst:
                amount = int(input("\nHow much was this expense?: "))
                self.users[self.user][self.prop]['roi']['cash on cash'][initial_expenses] = amount
            elif initial_expenses == 'q':
                break
            else:
                print('\nDoes not recognize input, please try again.')

        # Sum all investment expense values for total
        k = self.users[self.user][self.prop]['roi']['cash on cash']
        summation_c = sum(k.values())       
        self.users[self.user][self.prop]['roi']['cash on cash']['total investment'] = summation_c

        # Calculate ROI1
        if cash_flow*12 > 0 and summation_c > 0: 
            self.users[self.user][self.prop]['roi']['cash on cash']['ROI'] = ((cash_flow*12)/summation_c)*100
            roi = self.users[self.user][self.prop]['roi']['cash on cash']['ROI']
            print(f'\nYour ROI is {roi}%')


    def change_data(self):
        # print("""\n
        # --- What would you like to change? ---

        #         [1] Location Data
        #         [2] ROI Data

        # """)
        # selection = input('\nInput: ')
        # if selection == '1':
        #     pass
        # elif selection == '2':
        self.data_flag = False
        self.roi_info()
        self.data_flag = True


    def test_dict(self):
        print(f'\n{self.users}')


test1 = ROI_Calculator()

test1.start()

test1.test_dict()

