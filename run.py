from user import User
from credentials import Credentials

def create_users(username,password):
    new_user = User(username,password)
    return new_user

def save_users(user):
    user.save_user()

def delete_users(user):
    user.delete_user()

def find_user(username):
    return User.find_user_via_name(username)

def create_credentials(account,userName,password):
    new_credential = Credentials(account,userName,password)

def save_credentials(credentials):
    credentials.save_credentials()

def check_credential(account):
    return Credentials.credential_exist()

def find_credentials(account):
    return Credentials.find_credential(account)

def display_credentials():
    return Credentials.display_credentials() 

def delete_credentials(credentials):
    credentials.delete_credentials()

def generate_password():
    auto_password=Credentials.password_gen()
    return auto_password 

def verify_users():
    pass



def main():
    print("Welcome to password locker.Do you have an account?")
    print("Type YES to sign in , type NO to create a new account")
    have_account = input().lower()

    if have_account == "no":
        
        print("Create an account")    

        print("Intended username")
        username = input().lower()
        print('\n')

        print("Will you  have your generated?input YES to have it autogenerated.Input NO to create it yourself")
        
        response = input().lower()
        user_password = ''
        if response == "yes":
            user_password =user_password + generate_password()

        elif response == "no":
            print("type in your password")
            typed_password = input()
            user_password = user_password + typed_password

        save_users(create_users(username,user_password))
        print(f"Your username is {username} Your password is {user_password}")

    elif have_account == "yes":
        print("Enter username")
        username = input("username: ")
        print("Enter password")
        user_password=input("password: ")

        print(f"Hello {username}.Welcome To PassWord Locker Manager")  
        print('\n')


    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().upper()
        if short_code == "CC":
            print("Create new credentials")
            print("."*10)
            print("Account name")
            account = input("Account name: ")
            userName = input()
            password = ''

            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    input_password = input("Enter Your Own Password\n")
                    password = password + input_password
                    break
                elif password_Choice == 'gp':
                    generated_password = generate_password()
                    password = password + generated_password
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_credentials(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')


        

if __name__ == '__main__':

    main()    