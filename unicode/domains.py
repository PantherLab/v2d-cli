from .utils.unicode import to_hex, to_unicode
import random

latin_characters = [format(i + 32, '05x') for i in range(96)]


def similar_domain(domain, confusables):
    new_domain = ''
    for character in domain:
        character_hex = to_hex(character)
        if(character_hex not in latin_characters):
            new_domain = new_domain + character
        else:
            confusables_characters = confusables['characters'][character_hex]
            choice = random.choice(confusables_characters)
            new_domain = new_domain + to_unicode(choice)

    return new_domain
