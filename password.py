import string
import random
import pyperclip
class Password:

    password_letters = list(string.ascii_letters)
    password_nums = list(string.digits)
    password_symbols = ["#", "@", "&", "$", "%"]
    password_chars = []
    password_chars.extend(password_letters)
    password_chars.extend(password_nums)
    password_chars.extend(password_symbols)

    @classmethod
    def gene_password(cls):
        sys_password = "".join(random.sample(cls.password_chars, k=10))
        pyperclip.copy(sys_password)
        return sys_password
#obj = Credentials()
#print(obj.gen_password())
#print(obj.gen_password())