import random

def guess_random_number(tries, start, stop):
    random_int = random.randint(start, stop)
    while tries:
        guess = int(input('Enter a guess: '))
        if guess == random_int:
            print('Success!')
            return
        if guess < random_int:
            print('Guess higher!')
        else:
            print('Guess lower!')
        tries = tries - 1
    print('Failure')

def guess_random_num_linear(tries, start, stop):
    random_int = random.randint(start, stop)
    print(f'The number for the program to guess is: {random_int}')
    for x in range(start, stop + 1):
        if tries == 0:
            print('Program failure')
            return
        print(f'Number of tries left: {tries}')       
        print(f'The program is guessing... {x}')
        if x == random_int:
            print('The program has guess the correct number!')
            return
        tries = tries - 1

def guess_random_num_binary(tries, start, stop):
    lower_bound = start
    upper_bound = stop
    rand_int = random.randint(start, stop)
    print(f'Random number to find: {rand_int}')
    while tries:
        pivot = (lower_bound + upper_bound) // 2
        if pivot == rand_int:
            print(f'Found it! {rand_int}')
            return
        if pivot > rand_int:
            print('Guessing lower!')
            upper_bound = pivot - 1
        else:
            print('Guessing higher!')
            lower_bound = pivot + 1
        tries -= 1
    print('Your program failed to find the number.')



guess_random_number(5, 0, 10)   # test 1

# guess_random_num_linear(5, 0, 10)  #test 2

# guess_random_num_binary(5, 0, 100)  #test 3
