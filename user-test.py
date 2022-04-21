import unittest
from user import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.new_user = User("aust1inn","12345")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"aust1inn")
        self.assertEqual(self.new_user.password,"12345")


    def test_save_user(self):
        '''
        test_save_contact test case to test if the user object is saved into
         the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []    

    def test_delete_user(self):
        self.test_user = User("rael","54321")
        self.test_user.save_user()
        self.new_user.save_user()
        self.test_user.delete_user()
        self.assertEqual(len(User.user_list),1)

   

    # def test_find_user_by_name(self):
    #     """" 
    #     test to check if we can display the User information by searching with the username
    #     """ 
    #     self.new_user.save_user()
    #     self.test_user = User("rael","54321")
    #     self.test_user.save_user()

    #     user_found = User.find_user_via_name("rael")
    #     self.assertEqual(user_found.password, test_user.password)

if __name__ == '__main__':
    unittest.main()