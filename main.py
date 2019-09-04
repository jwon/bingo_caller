import os
import random


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


if __name__ == '__main__':
    input('WELCOME!')
    sequence = list(range(1, 101))
    random.shuffle(sequence)
    called_numbers = []
    os.system('clear')
    while True:
        for called_number in sequence:
            called_numbers.append(called_number)
            print(color.BOLD + color.PURPLE + 'ASHLEY AND EVA\'S BIRTHDAY BINGO!' + color.END)
            for i in range(1, 101):
                if i == called_number:
                    print(color.BLUE + color.BOLD + f'**{i}**' + color.END, end='')
                elif i in called_numbers:
                    print(color.RED + f'{strike(str(i))}' + color.END, end='')
                else:
                    print(i, end='')
                if i % 10 == 0:
                    print()
                else:
                    print('\t', end='')
            print()

            input(f'Remaining numbers: {len(sequence) - len(called_numbers)}')
            os.system('clear')
        break
