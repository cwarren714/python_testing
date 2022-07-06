import sys
import random
import pdb


def guess_game():
    if len(sys.argv) < 2:
        print('Enter two values when calling this program from the terminal')
        return
    start_num = int(sys.argv[1])
    second_num = int(sys.argv[2])
    correct_num = int(random.choice(range(start_num, second_num)))
    pdb.set_trace()

    while True:
        try:
            guess_num = int(
                input(f'Enter your guess between {start_num} and {second_num} : '))
            if int(guess_num) > 0 and int(guess_num) <= second_num:
                pass
        except ValueError:
            print('You must enter a number')
            continue
        if guess_num == correct_num:
            print('You got it!')
            return
        else:
            print('Nope, guess again!')


guess_game()
