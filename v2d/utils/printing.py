from colorama import Fore, Style


def print_green(text):
    print('{}{}{}'.format(Fore.GREEN, text, Style.RESET_ALL))


def print_red(text):
    print('{}{}{}'.format(Fore.RED, text, Style.RESET_ALL))
