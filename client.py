import credentials
class Client:
    """
    Class that generates new instances of account clients.
    """

    users_list = []

    def __init__ (self, username, password):
        '''
        Initialization method for a new client.
        ''' 
        self.username = username
        self.password = password
        self.credential = credentials.Credentials()

    @classmethod
    def add_user(cls, new_user):
        '''
        Method to add user to users_list.
        '''
        cls.users_list.append(new_user)

    @classmethod
    def check_login(cls, login_name, login_pass):
        '''
        Method to check if user login details exist in users_list.
        '''
        for user in cls.users_list:
            if user.username == login_name:
                if user.password == login_pass:
                    return True
        return False

    @classmethod
    def return_user(cls, username, password):
        '''
        Method to return user object upon successful login.
        '''
        for user in cls.users_list:
            if user.username == username:
                if user.password == password:
                    return user