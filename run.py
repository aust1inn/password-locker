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
