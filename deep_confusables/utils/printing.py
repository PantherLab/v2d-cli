from colorama import Fore, Style
from sys import stdout


def print_green(text):
    print('{}{}{}'.format(Fore.GREEN, text, Style.RESET_ALL))


def print_red(text):
    print('{}{}{}'.format(Fore.RED, text, Style.RESET_ALL))


def print_diff(domain, unicode_domain, is_tty=stdout.isatty()):
    # if len(domain) != len(unicode_domain) return(-1)

    difference = ''
    for i, letter in enumerate(unicode_domain):
        if letter != domain[i]:
            difference = difference + Fore.RED + letter
        else:
            difference = difference + Fore.GREEN + letter

    difference = difference + Style.RESET_ALL

    print(difference if is_tty else domain)
