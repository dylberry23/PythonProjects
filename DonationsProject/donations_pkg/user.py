def login(database, username, password):
    if username in database:
        if password == database[username]:
            print('Welcome back!')
            return username
        print('Password does not match username. Please try again.')
        return ''
    print('Username not found. Please register.')
    return ''
 

def register(database, username):
    if username in database:
        print('Username already registered.')
        return ''
    print('Username confirmed and registered.')
    return username