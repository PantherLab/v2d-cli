from .utils.unicode import to_hex, to_unicode
import random
from itertools import islice, product
import requests
import time
import whois
from virus_total_apis import PublicApi as VirusTotalPublicApi
import json

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


def get_confusables(x, confusables, latin_characters):
    return confusables['characters'][
                        to_hex(x)] if to_hex(x) in latin_characters else [
                                                                to_hex(x)]


def similar_domains(domain, confusables, max_domains=100000,):
    try:
        d = domain.split('.')
        domain = d[0]
        tld = d[1]

        characters_lists = [list(map(to_unicode,
                                     get_confusables(x,
                                                     confusables,
                                                     latin_characters)))
                            for x in domain]

        cartesian_product = product(*characters_lists)

        return [''.join(new_domain) + '.{}'.format(tld)
                for new_domain in islice(cartesian_product, max_domains)]

    except IndexError:
        print('The domain must contain a dot.')
        return []


def check_domain(domain, API_KEY, t=5, verbose=False, whois=False, vt=False):
    try:
        requests.get('https://{}'.format(domain))
        if verbose:
            print('The domain {} exists'.format(domain))
        if whois:
            w = who_is(domain)
            if(w is not None):
                print(w)
        if vt:
            vt = VirusTotalPublicApi(API_KEY)
            response = vt.get_url_report('https://{}'.format(domain), scan='1')
            print(json.dumps(response, sort_keys=False, indent=4))
    except Exception:
        if verbose:
            print('The domain {} does not exist'.format(domain))
    time.sleep(t)


def check_domains(domains, API_KEY, t=5, verbose=False, whois=False, vt=False):
    for domain in domains:
        check_domain(domain, API_KEY, t, verbose, whois, vt)


def who_is(domain):
    try:
        return whois.whois(domain)
    except whois.parser.PywhoisError:
        print('Whois not found!')
