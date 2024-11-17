import random

random_digit = random.randint(0, 9)
count_guess = 0
max_guess = 3

while count_guess < max_guess:
    user_input = int(input('Guess a digit: '))
    count_guess += 1
    if user_input == random_digit:
        print('Congrats !! You guessed the right digit.')
        break
else:
    print('Sorry, you are out of chances :)')
    print(f'The random digit was {random_digit}')