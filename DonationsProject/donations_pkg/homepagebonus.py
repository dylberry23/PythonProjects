def show_homepage():
    print("")
    print("          === Donate Me Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations       |")
    print("------------------------------------------")
    print('|              5.   Exit                 |        ')
    print("------------------------------------------")

def donate(username):
    amount = float(input('Enter amount to donate: '))
    donation_string = (f'{username} donated ${amount}')
    print('Thank you for your donation!')
    return donation_string

def show_donations(donations):
    print('\n---All Donations---')
    if donations == 0:
        print('Currently, there are no donations.')
    else:
        total = 0
        for donation in donations:
            print(donation)
            idx = donation.find('$') + 1
            total += float(donation[idx:])
        print('Total = $' + str(total))