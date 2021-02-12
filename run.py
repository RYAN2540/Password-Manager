#!/usr/bin/env python3.9
from credentials import Credentials
from client import Client
credential = Credentials()

def sign_up():

    username_signup = ""
    password_signup = ""

    print("----Sign up here----")
    username_valid = True
    while username_valid:
        username_signup = input("Username: ")
        if len(username_signup)<5:
            username_valid = True
            print("Username too short. Try again.")
        else:
            username_valid = False

    want_password_valid = True
    while want_passowrd_valid:
        want_sys_password = input("Want system generated password? (Yes/No): ")
        if want_sys_password == "Yes":
            want_password_valid = False
            password_signup = credential.gene_password()
            print("Your password: "+password_signup)
        elif want_sys_password == "No":
            password_signup = input("Password (at least 5 chars): ")
            password_confirm = input("Confirm password: ")
            if len(password_signup)<5:
                want_password_valid = True
                print("Password too short. Try again.")
            elif password_confirm == password_signup:
                print(username_signup)
                print("Your password: "+password_confirm)
                want_password_valid = False
            else:
                print("Passwords did not match. Try again.")
                want_password_valid = True
        else:
            print("Invalid choice. Choose Yes/No")
            want_password_valid = True

    new_user=User(username_signup,password_signup)
    new_user.add_user(new_user)

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

