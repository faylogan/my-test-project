# create record
# update record
# read record
# delete record
# CURD
# find user

def create(account_number, user_details):

    
    f = open("data/user_record/" + str(account_number) + ".txt", "x")
    f.write(str(user_details))
    f.write(str(user_details))
    f.close()


    # create a file
    # name of the file will be account_number.txt
    # add the user details to the file
    # return true
    # is saving to file fails, delete created file

def read(user_account_number):
    print("read user record")
    # find user with account number
    # fetch content of the file

def update(user_account_number):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true

def delete(user_account_number):
    print("delete user record")
    # find user with account number
    # delete the user record (file)
    # return true

def find(user_account_number):
    print("find user")
    # find user record in data folder


    create(456789,['Fay', 'Logan', 'password', ])