#!/usr/bin/env python3.9
from credentials import Credentials
from client import Client
credential = Credentials()

def sign_up():
    print("----Sign up here----")
    username_signup = input("Username: ")
    want_password_valid = True
    while want_passowrd_valid:
        want_sys_password = input("Want system generated password? (Yes/No): ")
        if want_sys_password == "Yes":
            want_password_valid = False
            your_password = credential.gene_password()
            print("Your password: "+your_password)
        elif want_sys_password == "No":
            password_signup = input("Password: ")
            password_confirm = input("Confirm password: ")
            if password_confirm == password_signup:
                print(username_signup)
                print("Your password: "+password_confirm)
                want_password_valid = False
            else:
                print("Passwords did not match. Try again.")
                want_password_valid = True
        else:
            print("Invalid choice. Choose Yes/No")
            want_password_valid = True


def login():
    print("----Login Here----")
    username_login = input("Username: ")
    password_login = input("Password: ")
    print(username_login)
    print(password_login)


def main():
    print("PASSWORD MANAGER")
    print("="*15)
    has_account_valid = True
    while has_account_valid:
        has_account = input("Have an account? (Yes/No): ")
        if has_account == "Yes":
            has_account_valid = False
            login()
        elif has_account == "No":
            has_account_valid = False
            sign_up()
        else:
            print("Invalid choice. Choose Yes/No")
            has_account_valid = True


if __name__ == "__main":
    main ()

