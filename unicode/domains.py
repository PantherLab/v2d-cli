from .utils.unicode import to_hex, to_unicode
import random
from itertools import islice, product

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


def similar_domains(domain, confusables, max_domains=100000):
    characters_lists = [list(map(to_unicode,
                                 confusables['characters'][to_hex(x)]
                                 )) for x in domain]

    cartesian_product = product(*characters_lists)

    return [''.join(new_domain) for new_domain in islice(cartesian_product,
                                                         max_domains)]
