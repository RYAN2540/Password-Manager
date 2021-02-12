#!/usr/bin/env python3.9
import Password
import Client
#from credentials import Credentials
password_obj = password.Password()

def sign_up():

    username_signup = ""
    password_signup = ""

    print("")
    print("----Sign up here----")
    username_valid = True
    while username_valid:
        username_signup = input("Username (at least 5 chars): ")
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
            password_signup = password_obj.gene_password()
            print("Sign up successful")
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
                print("Signup successful")
                want_password_valid = False
            else:
                print("Passwords did not match. Try again.")
                want_password_valid = True
        else:
            print("Invalid choice. Choose Yes/No")
            want_password_valid = True

    new_user=user.User(username_signup,password_signup)
    new_user.add_user(new_user)
    login()

def login():
    is_login=True
    while is_login:
        print("\")
        print("-----Log in here-----")
        username_login = input("Username: ")
        password_login = input("Password: ")
        login_valid = user.User.check_login(username_login, password_login)
        if login_valid:
            print("Login successful!")
            is_login=False
            user_obj = User.return_user(username_login, password_login)
            account_menu(usernam_login, user_obj)
        else:
            print("Login unsuccessful. Try again.")
            is_login=True


def account_menu(this_user_name, this_user_object):
    print("*"*45)
    # print(" ")
    print(f'WELCOME TO YOUR ACCOUNT, {this_user_name.upper()}')
    print("Options menu")
    print("1. Add existing credential - press 1")
    print("2. Create new credential   - press 2")
    print("3. View saved credentials  - press 3")
    print("4. Delete saved credential - press 4")
    print("5. Log out                 - press 5")


    is_selected=True
    while is_selected:
        print(" ")
        selected=input("What do you want to do? Press option: ")
        if selected=="1":
            is_selected = True
            this_user_object.credential.add_credential()
        elif selected=="2":
            is_selected = True
            this_user_object.credential.create_credential()
        elif selected=="3":
            is_selected = True
            this_user_object.credential.view_credentials()
        elif selected=="4":
            is_selected = True
            this_user_object.credential.delete_credential()
        elif selected=="5":
            is_selected = False
            logout()
            print("LOGGED OUT.")
        else:
            print("Invalid option. Try again.")
            is_selected=True


def main():
    print("PASSWORD MANAGER")
    print("="*15)
    proceed = "1"
    to_proceed = True
    while to_proceed:
        proceed = input("Press 1 to login or 0 to exit: ")
        if proceed == "1":
            to_proceed = True

            has_account_valid = True    
            while has_account_valid:                
                has_account = input("Have an account? (Yes/No): ")
                if has_account == "Yes":            
                    login()
                    has_account_valid = False
                elif has_account == "No":            
                    sign_up()
                    has_account_valid = False
                else:
                    print("Invalid choice. Choose Yes/No")
                    has_account_valid = True

        elif proceed == "0":
            to_proceed = False
        else:
            print("Invalid option")
            to_proceed = True
    print("----BYE----")


if __name__ == "__main":
    main ()

