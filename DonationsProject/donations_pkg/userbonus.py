def login(database, username, password):
    if username.lower() in database:
        if password == database[username]:
            print('Welcome back', username + '!')
            return username
        print('Password does not match username. Please try again.')
        return ''
    print('Username not found. Please register.')
    return ''
 

def register(database, username, password):
    if username.lower() in database:
        print('Username already registered.')
        return ''
    if len(username) > 10:
        print('Username cannot be over 10 characters.')
        return ''
    if len(password) <= 5:
        print('Password must bo at least 5 characters.')
        return ''

    print('\nUsername' + username, 'registered!')
    return username

    