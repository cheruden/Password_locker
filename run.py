from user_cred_classes import Users, Credentials

def create_user(first,last,pwd):
    '''
    creates a new user account
    '''
    user_new= Users(first,last,pwd)
    return user_new
def register_user(user):
    '''
    saves the created user's account
    '''
    Users.create_user(user)

def user_check(first,pwd):
    '''
    checks whether user exists before creating account
    '''
