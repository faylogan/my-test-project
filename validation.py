def account_number_validation(account_number):

    if account_number:


            try:
                int(account_number)
            
                if len(str(account_number)) == 6:
                    return True

            except ValueError:
                print("Invalid account number please try again")
                return False
            except TypeError:
                print("Invalid account type")
                return False
            
    return False