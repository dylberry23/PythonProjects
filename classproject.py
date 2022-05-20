class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password, balance = 0.0):
        super().__init__(name, pin, password)
        self.balance = balance
        self.show_balance()

    def show_balance(self):
        print(f'{self.name} has an account balance of: {self.balance}')

    def withdraw(self, withdraw_amt):
        self.balance -= withdraw_amt
        return self.balance
        print

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        return self.balance

    def transfer_money(self, transfer_amt, receiving_user):
        print(f'You are transferring {transfer_amt} to {receiving_user.name}')
        print('Authentication Required')
        pin_code = input('Enter your PIN: ')
        if pin_code == self.pin:
            self.balance -= transfer_amt
            self.show_balance()
            receiving_user.balance += transfer_amt
            receiving_user.show_balance()
            return True
        print('Invalid PIN')
        return False
    
    def request_money(self, request_amt, requesting_user):
        print(f'You are requesting {request_amt} from {requesting_user.name}')
        print('Authentication Required')
        pin_code = input(f'Enter {requesting_user.name}\'s PIN: ')
        user_password = input('Enter your password: ')
        if pin_code == self.pin:
            if user_password == requesting_user.password:
                self.balance += request_amt
                requesting_user.balance -= request_amt
                print('Request authorized')
                print(f'{requesting_user.name} sent {request_amt}')
                self.show_balance()
                requesting_user.show_balance()
                return True
        print('Invalid PIN')
        return False
              





    # def request_money(self, request_amt, test_pin):
    #     if test_pin == self.pin:


# Driver Code for Task 1

# test1 = User('Bob', '1234', 'password')
# print(test1.name, test1.pin, test1.password)


# Driver Code for Task 2

# test2 = User('Bob', '1234', 'password')
# print(test2.name, test2.pin, test2.password)
# test2.change_name('Bobby')
# test2.change_pin('4321')
# test2.change_password('newpassword')
# print(test2.name, test2.pin, test2.password)

# Driver Code for Task 3

# test3 = BankUser('Bob', '1234', 'password')
# print(test3.name, test3.pin, test3.password, test3.balance)

# Driver Code for Task 4

# test4 = BankUser('Bob', '1234', 'password')
# test4.show_balance()
# test4.deposit(float(1000))
# test4.show_balance()
# test4.withdraw(float(500))
# test4.show_balance()

# Driver Code for Task 5
bob = BankUser('Alice', '1234', 'password', 5000)
alice = BankUser('Bob', '1234', 'password')
bob.transfer_money(500,alice)
alice.request_money(250, bob)