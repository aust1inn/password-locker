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
        pass

    def test_save_user(self):
        pass

    def test_delete_user(self):
        pass

    def test_user_exists(self):
        pass

    def test_find_user_by_name(self):
        pass    

if __name__ == '__main__':
    unittest.main()