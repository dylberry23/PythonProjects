from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {'admin': "password123", 'donation': 'amount'}
donations = []
authorized_user = ''

show_homepage()

if authorized_user == '':
    print('You must be logged in to donate.')
else:
    print('Logged in as:', authorized_user)

while True:
    menu_selection = input('Choose options 1 - 5: ')
    if menu_selection == '1':
        username = input('Enter Username: ')
        password = input('Enter password: ')
        authorized_user = login(database, username, password)

    elif menu_selection == '2':
        username = input('Enter Username: ')
        password = input('Enter password: ')
        authorized_user = register(database, username, password)
        if authorized_user != '':
            database[authorized_user] = password

    elif menu_selection == '3':
        if authorized_user == '':
            print('You are not logged in.')
        donation_string = donate(authorized_user)
        donations.append(donation_string)    

    elif menu_selection == '4':
        show_donations(donations)
        
    elif menu_selection == '5':
        print('Goodbye!')
        break
