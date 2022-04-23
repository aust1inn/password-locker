import getpass
import pyperclip
import random
import string

class Credentials:
    """
    Create credentials class to help create new objects of credentials
    """

    credentials_list =[]

    def __init__(self,account,userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password

    def save_credentials(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)    

    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """   

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list            

    @classmethod
    def credential_exist(cls,account):
        """"
        Checks if credential exists by passing the account name
        """            
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            return False    

    @classmethod
    def copy_credentials(cls,account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials)

    def password_gen():
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        size = 0
        password = ''
        while size <8:
            password = password + random.choice(characters)
            size +=1

        return password

    if __name__ == '__main__':

        password_gen()         