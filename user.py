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