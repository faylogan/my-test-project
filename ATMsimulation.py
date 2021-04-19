# register
# first name, last name, email, password
# generate user account


# login
# account number, password


#bank operations

#Initalizing the system
import random
import validation
import database


def init():
    print('Welcome to bank Python')

    
    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))
    
    if have_account == 1:
        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected an invalid option")
        init()


def login():

    print("***** Login *****")


    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = input("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operations(user)

        print('Invalid account or password')
        login()
    else:
        print("Account number invalid")
        init ()



def register():

    print("**** Register ****")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Please create a password? \n")

    
    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your account has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("There is someting wrong, please try again")
        register()


    
def bank_operations(user):

    print("Welcome %s %s" % ( user[0], user[1]) )

    from datetime import datetime

    now = datetime.now()
        
    print("now =", now)

    selected_option = int(input("What would you like to do? (1) withdrawal (2) deposit (3) Logout (4) Exit \n"))

    if(selected_option == 1):
        withdrawal_operation()

    elif(selected_option == 2):
        deposit_operation()

    elif(selected_option == 3):
        login()

    elif(selected_option == 4):
        exit()

    else:
        print('Invalid option selected')
        bank_operations(user)


def withdrawal_operation():
    print("**Withdrawal**")
    print('How much would you like to withdraw:')
    withdrawal = int(input('Please type in your response. \n'))
    print('Please take your cash')
    print("Your new balance is:")
    import random
    print(random.randrange(100,500))
    print("Back to the Main menu")
    login()
    
def deposit_operation():
    print("**Deposit**")
    print("How much would you like to deposit?")
    deposit = int(input('Please make your deposit here \n'))
    print("Your current balance is:")
    import random
    print(random.randrange(1000,10000))
    print("Back to the Main menu")
    login()
        
def generation_account_number():

    return random.randrange(111111,999999)


def set_current_balance(user, balance):
    user[4] = balance


def get_current_balance(user):
    return user[4]

def logout():
    login()



#### ACTUAL BANKING SYSTEM ####

init()