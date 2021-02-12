from client.py import client
import string
import random
class Credentials:

    password_letters = list(string.ascii_letters)
    password_nums = list(string.digits)
    password_symbols = ["#", "@", "&", "$", "%"]
    password_chars = []
    password_chars.extend(password_letters)
    password_chars.extend(password_nums)
    password_chars.extend(password_symbols)


    def gene_password(self):
        sys_password = "".join(random.sample(self.password_chars, k=10))
        return sys_password


obj=Credentials()
print(obj.gene_password())