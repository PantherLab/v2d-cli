import argparse
import configparser

from .domains import similar_domains
from .utils.similarity import load_file

config = configparser.ConfigParser()
config.read('config')

DESCRIPTION = config['APPLICATION_INFO']['DESCRIPTION']


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('domain', action='store',
                        help='check similar domains to this one')
    args = parser.parse_args()

    confusables = load_file()

    domains = similar_domains(args.domain, confusables)
    print('Similar domains to {}'.format(args.domain))
    for d in domains:
        print(d)


if __name__ == 'main':
    main()
