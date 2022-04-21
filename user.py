from unicodedata import name

from importlib_metadata import method_cache


class User:
    """""
    Creates user class that will generate users instances

    """""

    user_list=[]

    def __init__(self,username,password):
        self.username=username
        self.password=password

    def save_user(self):
        """""  
        Saves user by appending them into the user_list list

        """""

        User.user_list.append(self)

    @classmethod
    def find_user_via_name(cls,username):
        """"" 
        A method that will find a user by name

        args:username

        """""   
        for user in cls.user_list:
            if User.username == username:
                return user

    def delete_user (self):
        """""
        Deletes user from user_list by the remove method

        """""
        User.user_list.remove(self)


        