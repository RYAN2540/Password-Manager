import unittest
import pyperclip
from account import Account

class AppTest(unittest.TestCase):
    def setUp(self):
        self.account_obj=Account("Gmail", "Ryan", "austinbrian005")

    def tearDown(self):
        pass

    def test_account_init(self):
        self.assertEqual(self.account_obj.acc_nm, "Gmail")
        self.assertEqual(self.account_obj.acc_uname, "Ryan")
        self.assertEqual(self.account_obj.acc_pass, "austinbrian005")        


if __name__=='__main__':
    unittest.main()