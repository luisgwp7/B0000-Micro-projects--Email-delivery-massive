def user_requirents(requirement):
    '''
    Invoques the user email and the password id
    '''
    if requirement == 'User':
        return_request = 'your_email@gmail.com'
    elif requirement == 'Password':
        return_request = 'your_password_id_gmail'
    else: 
        print('The requirements must be "User" or "Password"')
    
    return return_request

