import re
import sys
from colorama import Fore

def is_valid(password):

    if len(password) < 10:
        print(Fore.RED + "password length below 10")
        return False

    if not re.search('[a-zA-Z]', password):
        print(Fore.RED + "password doesn't have letters")
        return False

    if not re.search('[0-9]', password):
        print(Fore.RED + "password doesn't have numbers")
        return False

    if not re.search('[a-z]', password):
        print(Fore.RED + "password doesn't have small capital case")
        return False
    
    if not re.search('[A-Z]', password):
        print(Fore.RED + "password doesn't have big capital case")
        return False

    return True


if __name__ == "__main__":

    if is_valid(sys.argv[1]):
        print(Fore.GREEN + "password is valid")
        exit(0)
    else:
        exit(1)